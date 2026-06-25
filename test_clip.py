from src.vlm_tokens.clip_features import CLIPFeatureExtractor

# Create extractor
extractor = CLIPFeatureExtractor()

# Change this to one of your KITTI images
image_path = r"D:\hazy-vlm-optical-flow\datasets\kitti_light_eval\training\image_2\000000_10.png"

features = extractor.extract_image_features(image_path)

print("Feature shape:", features.shape)
print(features)