from pathlib import Path

ROOT = Path("D:/hazy-vlm-optical-flow/datasets")


def count_files(path, pattern):
    path = Path(path)

    if not path.exists():
        return 0

    return len(list(path.rglob(pattern)))


print("=" * 50)
print("DATASET INVENTORY")
print("=" * 50)

# ==========================
# KITTI
# ==========================
print("\nKITTI")

kitti_images = count_files(
    ROOT / "kitti" / "training" / "image_2",
    "*.png"
)

kitti_flow = count_files(
    ROOT / "kitti" / "training" / "flow_occ",
    "*.png"
)

kitti_disp = count_files(
    ROOT / "kitti" / "training" / "disp_occ_0",
    "*.png"
)

print(f"Images     : {kitti_images}")
print(f"Flow Files : {kitti_flow}")
print(f"Disparity  : {kitti_disp}")

# ==========================
# SINTEL
# ==========================
print("\nSINTEL")

sintel_clean = count_files(
    ROOT / "sintel" / "training" / "clean",
    "*.png"
)

sintel_final = count_files(
    ROOT / "sintel" / "training" / "final",
    "*.png"
)

sintel_flow = count_files(
    ROOT / "sintel" / "training" / "flow",
    "*.flo"
)

print(f"Clean Images : {sintel_clean}")
print(f"Final Images : {sintel_final}")
print(f"Flow Files   : {sintel_flow}")

print("\n" + "=" * 50)