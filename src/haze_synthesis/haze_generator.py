import cv2
import numpy as np
import json
from pathlib import Path

KITTI_ROOT = Path(
    "D:/hazy-vlm-optical-flow/datasets/kitti/training"
)

# --------------------------------------------------
# Load KITTI Pair
# --------------------------------------------------

image1_path = KITTI_ROOT / "image_2" / "000000_10.png"
image2_path = KITTI_ROOT / "image_2" / "000000_11.png"

disp_path = KITTI_ROOT / "disp_occ_0" / "000000_10.png"

image1 = cv2.imread(str(image1_path))
image2 = cv2.imread(str(image2_path))

disparity = cv2.imread(
    str(disp_path),
    cv2.IMREAD_UNCHANGED
).astype(np.float32)

# --------------------------------------------------
# Disparity -> Depth
# --------------------------------------------------

valid_mask = disparity > 0

depth = np.zeros_like(disparity, dtype=np.float32)

depth[valid_mask] = 1.0 / disparity[valid_mask]

d_min = depth[valid_mask].min()
d_max = depth[valid_mask].max()

depth[valid_mask] = (
    depth[valid_mask] - d_min
) / (
    d_max - d_min
)

depth[~valid_mask] = 1.0

depth = cv2.GaussianBlur(
    depth,
    (21, 21),
    0
)

# Save depth visualization
depth_vis = (depth * 255).astype(np.uint8)
cv2.imwrite(
    "depth_visualization.png",
    depth_vis
)

# --------------------------------------------------
# Haze Levels
# --------------------------------------------------

HAZE_LEVELS = {
    "clear": 0.0,
    "light": 0.2,
    "medium": 0.5,
    "dense": 0.8,
    "extreme": 1.2
}

# Random atmospheric light
A_value = np.random.uniform(0.75, 0.95)

A = np.array([
    A_value,
    A_value,
    A_value
])

image1_float = image1.astype(np.float32) / 255.0
image2_float = image2.astype(np.float32) / 255.0

# --------------------------------------------------
# Generate Hazy Pair
# --------------------------------------------------

for haze_name, beta in HAZE_LEVELS.items():

    t = np.exp(-beta * depth)

    t_rgb = np.repeat(
        t[:, :, np.newaxis],
        3,
        axis=2
    )

    hazy1 = image1_float * t_rgb + A * (1 - t_rgb)
    hazy2 = image2_float * t_rgb + A * (1 - t_rgb)

    hazy1 = np.clip(
        hazy1 * 255,
        0,
        255
    ).astype(np.uint8)

    hazy2 = np.clip(
        hazy2 * 255,
        0,
        255
    ).astype(np.uint8)

    output1 = f"{haze_name}_10.png"
    output2 = f"{haze_name}_11.png"

    cv2.imwrite(output1, hazy1)
    cv2.imwrite(output2, hazy2)

    metadata = {
        "pair_id": "000000",
        "image1": "000000_10",
        "image2": "000000_11",
        "dataset": "KITTI",
        "haze_level": haze_name,
        "beta": beta,
        "atmospheric_light": float(A_value)
    }

    with open(
        f"{haze_name}_metadata.json",
        "w"
    ) as f:
        json.dump(
            metadata,
            f,
            indent=4
        )

    print(
        f"Saved {output1}, {output2}"
    )

print("Done!")