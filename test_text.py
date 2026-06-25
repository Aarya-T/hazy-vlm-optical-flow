from src.vlm_tokens.text_prompts import CLIPTextEncoder

encoder = CLIPTextEncoder()

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

features = encoder.encode_prompts(prompts)

print("Feature shape:", features.shape)
print(features)