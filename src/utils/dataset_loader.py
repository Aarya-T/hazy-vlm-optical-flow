from pathlib import Path


class KITTIDataset:
    def __init__(self, root):
        self.root = Path(root)

        self.image_dir = self.root / "image_2"
        self.flow_dir = self.root / "flow_occ"
        self.disp_dir = self.root / "disp_occ_0"

        self.images = sorted(list(self.image_dir.glob("*.png")))

    def __len__(self):
        return len(self.images) // 2

    def __getitem__(self, idx):

        image1 = self.image_dir / f"{idx:06d}_10.png"
        image2 = self.image_dir / f"{idx:06d}_11.png"

        flow = self.flow_dir / f"{idx:06d}_10.png"
        disparity = self.disp_dir / f"{idx:06d}_10.png"

        return {
            "image1": str(image1),
            "image2": str(image2),
            "flow": str(flow),
            "disparity": str(disparity),
            "dataset_name": "KITTI",
            "sample_id": idx
        }


if __name__ == "__main__":

    dataset = KITTIDataset(
        "D:/hazy-vlm-optical-flow/datasets/kitti/training"
    )

    print("Dataset size:", len(dataset))

    sample = dataset[0]

    for k, v in sample.items():
        print(k, ":", v)