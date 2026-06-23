from pathlib import Path
import json


class KITTIDataset:

    def __init__(
        self,
        kitti_root,
        hazy_root=None,
        haze_level="medium"
    ):

        self.kitti_root = Path(kitti_root)

        self.image_dir = (
            self.kitti_root / "image_2"
        )

        self.flow_dir = (
            self.kitti_root / "flow_occ"
        )

        self.disp_dir = (
            self.kitti_root / "disp_occ_0"
        )

        self.hazy_root = (
            Path(hazy_root)
            if hazy_root
            else None
        )

        self.haze_level = haze_level

        self.images = sorted(
            list(
                self.image_dir.glob("*.png")
            )
        )

    def __len__(self):

        return len(self.images) // 2

    def __getitem__(self, idx):

        pair_id = f"{idx:06d}"

        sample = {

            "clean_image1":
                str(
                    self.image_dir /
                    f"{pair_id}_10.png"
                ),

            "clean_image2":
                str(
                    self.image_dir /
                    f"{pair_id}_11.png"
                ),

            "flow":
                str(
                    self.flow_dir /
                    f"{pair_id}_10.png"
                ),

            "disparity":
                str(
                    self.disp_dir /
                    f"{pair_id}_10.png"
                ),

            "dataset_name":
                "KITTI",

            "sample_id":
                idx
        }

        if self.hazy_root:

            sample[
                "hazy_image1"
            ] = str(
                self.hazy_root /
                self.haze_level /
                f"{pair_id}_10.png"
            )

            sample[
                "hazy_image2"
            ] = str(
                self.hazy_root /
                self.haze_level /
                f"{pair_id}_11.png"
            )

            metadata_file = (
                self.hazy_root /
                "metadata" /
                f"{pair_id}_{self.haze_level}.json"
            )

            if metadata_file.exists():

                with open(
                    metadata_file,
                    "r"
                ) as f:

                    sample[
                        "metadata"
                    ] = json.load(f)

        return sample


if __name__ == "__main__":

    dataset = KITTIDataset(
        kitti_root=
        "D:/hazy-vlm-optical-flow/datasets/kitti/training",

        hazy_root=
        "D:/hazy-vlm-optical-flow/datasets/kitti_hazy",

        haze_level="medium"
    )

    print(
        "Dataset size:",
        len(dataset)
    )

    sample = dataset[0]

    for k, v in sample.items():

        print(
            k,
            ":",
            v
        )