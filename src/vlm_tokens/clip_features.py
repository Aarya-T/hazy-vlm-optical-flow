import torch
import open_clip
from PIL import Image


class CLIPFeatureExtractor:
    def __init__(self, device=None):
        # Use GPU if available
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Load pretrained OpenCLIP model
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            "ViT-B-32",
            pretrained="laion2b_s34b_b79k"
        )

        self.model.eval()
        self.model.to(self.device)

    @torch.no_grad()
    def extract_image_features(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.preprocess(image).unsqueeze(0).to(self.device)

        features = self.model.encode_image(image)

        # Normalize feature vector
        features = features / features.norm(dim=-1, keepdim=True)

        return features.cpu()