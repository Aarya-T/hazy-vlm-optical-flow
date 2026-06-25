from src.vlm_tokens.clip_features import CLIPFeatureExtractor
from src.vlm_tokens.global_token import GlobalHazeToken

# Path to a test image
image_path = r"D:\hazy-vlm-optical-flow\datasets\kitti\training\image_2\000000_10.png"

# Load CLIP feature extractor
clip = CLIPFeatureExtractor()

# Extract image embedding
image_embedding = clip.extract_image_features(image_path)

# Create global token module
token_generator = GlobalHazeToken()

# Generate token
global_token = token_generator(image_embedding)

# Print results
print("Image Embedding Shape:", image_embedding.shape)
print("Global Token Shape:", global_token.shape)
print("\nFirst 10 values of Global Token:")
print(global_token[0][:10])