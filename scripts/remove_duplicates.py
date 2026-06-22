import cv2
import numpy as np
from pathlib import Path
import shutil

FRAME_DIR = Path("D:/hazy-vlm-optical-flow/datasets/real_fog/frames")
OUTPUT_DIR = Path("D:/hazy-vlm-optical-flow/datasets/real_fog/cleaned")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

THRESHOLD = 5.0

for video_folder in FRAME_DIR.iterdir():

    if not video_folder.is_dir():
        continue

    save_folder = OUTPUT_DIR / video_folder.name
    save_folder.mkdir(exist_ok=True)

    previous = None
    kept = 0

    for image_path in sorted(video_folder.glob("*.jpg")):

        image = cv2.imread(str(image_path))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if previous is None:
            shutil.copy(image_path, save_folder / image_path.name)
            previous = gray
            kept += 1
            continue

        diff = np.mean(np.abs(gray.astype(float) - previous.astype(float)))

        if diff > THRESHOLD:
            shutil.copy(image_path, save_folder / image_path.name)
            previous = gray
            kept += 1

    print(f"{video_folder.name}: kept {kept} frames")

print("Done!")