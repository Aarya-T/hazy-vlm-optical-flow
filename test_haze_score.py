from src.vlm_tokens.clip_features import CLIPFeatureExtractor
from src.vlm_tokens.text_prompts import CLIPTextEncoder
from src.vlm_tokens.haze_similarity import HazeSimilarity
from src.vlm_tokens.haze_score import GlobalHazeScore

image_path = r"D:\hazy-vlm-optical-flow\datasets\kitti_extreme_eval\training\image_2\000000_10.png"

prompts = [
    "a hazy low visibility image",
    "a dense foggy outdoor scene",
    "an image with low contrast due to haze",
    "distant objects are obscured by fog",

    "a clear sharp high visibility image",
    "a clean outdoor image",
    "an image with clear distant objects",
    "a high contrast clear scene"
]

image_encoder = CLIPFeatureExtractor()
text_encoder = CLIPTextEncoder()

image_features = image_encoder.extract_image_features(image_path)
text_features = text_encoder.encode_prompts(prompts)

similarities = HazeSimilarity.compute_similarity(
    image_features,
    text_features
)

score = GlobalHazeScore.compute(similarities)

print("\nGlobal Haze Score:", score)