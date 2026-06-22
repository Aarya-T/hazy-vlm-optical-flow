import cv2
from pathlib import Path

VIDEO_DIR = Path("D:/hazy-vlm-optical-flow/datasets/real_fog/videos")
OUTPUT_DIR = Path("D:/hazy-vlm-optical-flow/datasets/real_fog/frames")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FRAME_SKIP = 30  # save 1 frame every 30 frames

for video_path in VIDEO_DIR.glob("*.mp4"):

    video_name = video_path.stem
    save_dir = OUTPUT_DIR / video_name
    save_dir.mkdir(exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % FRAME_SKIP == 0:
            output_file = save_dir / f"frame_{saved_count:05d}.jpg"
            cv2.imwrite(str(output_file), frame)
            saved_count += 1

        frame_count += 1

    cap.release()

    print(f"{video_name}: saved {saved_count} frames")

print("Done!")