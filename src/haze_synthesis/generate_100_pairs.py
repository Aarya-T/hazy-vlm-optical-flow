import cv2
import numpy as np
import json
from pathlib import Path

KITTI_ROOT = Path(
    "D:/hazy-vlm-optical-flow/datasets/kitti/training"
)

OUTPUT_ROOT = Path(
    "D:/hazy-vlm-optical-flow/datasets/kitti_hazy"
)

# Create output folders
for level in ["light", "medium", "dense", "extreme"]:
    (OUTPUT_ROOT / level).mkdir(
        parents=True,
        exist_ok=True
    )

(OUTPUT_ROOT / "metadata").mkdir(
    parents=True,
    exist_ok=True
)

HAZE_LEVELS = {
    "light": 0.2,
    "medium": 0.5,
    "dense": 0.8,
    "extreme": 1.2
}

# First 100 KITTI pairs
for sample_id in range(200):

    pair_name = f"{sample_id:06d}"

    image1_path = (
        KITTI_ROOT /
        "image_2" /
        f"{pair_name}_10.png"
    )

    image2_path = (
        KITTI_ROOT /
        "image_2" /
        f"{pair_name}_11.png"
    )

    disparity_path = (
        KITTI_ROOT /
        "disp_occ_0" /
        f"{pair_name}_10.png"
    )

    # Skip missing files
    if (
        not image1_path.exists()
        or not image2_path.exists()
        or not disparity_path.exists()
    ):
        print(
            f"Skipping {pair_name}"
        )
        continue

    image1 = cv2.imread(
        str(image1_path)
    )

    image2 = cv2.imread(
        str(image2_path)
    )

    disparity = cv2.imread(
        str(disparity_path),
        cv2.IMREAD_UNCHANGED
    ).astype(np.float32)

    # ----------------------------------
    # Disparity -> Depth
    # ----------------------------------

    valid_mask = disparity > 0

    depth = np.zeros_like(
        disparity,
        dtype=np.float32
    )

    depth[valid_mask] = (
        1.0 /
        disparity[valid_mask]
    )

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

    image1_float = (
        image1.astype(np.float32)
        / 255.0
    )

    image2_float = (
        image2.astype(np.float32)
        / 255.0
    )

    # Random atmosphere
    A_value = np.random.uniform(
        0.75,
        0.95
    )

    A = np.array([
        A_value,
        A_value,
        A_value
    ])

    for haze_name, beta in HAZE_LEVELS.items():

        t = np.exp(
            -beta * depth
        )

        t_rgb = np.repeat(
            t[:, :, np.newaxis],
            3,
            axis=2
        )

        hazy1 = (
            image1_float * t_rgb
            + A * (1 - t_rgb)
        )

        hazy2 = (
            image2_float * t_rgb
            + A * (1 - t_rgb)
        )

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

        output_folder = (
            OUTPUT_ROOT /
            haze_name
        )

        cv2.imwrite(
            str(
                output_folder /
                f"{pair_name}_10.png"
            ),
            hazy1
        )

        cv2.imwrite(
            str(
                output_folder /
                f"{pair_name}_11.png"
            ),
            hazy2
        )

        metadata = {
            "pair_id": pair_name,
            "dataset": "KITTI",
            "haze_level": haze_name,
            "beta": beta,
            "atmospheric_light": float(
                A_value
            )
        }

        with open(
            OUTPUT_ROOT
            / "metadata"
            / f"{pair_name}_{haze_name}.json",
            "w"
        ) as f:

            json.dump(
                metadata,
                f,
                indent=4
            )

    print(
        f"Generated pair {pair_name}"
    )

print(
    "Finished generating first 200 KITTI pairs."
)