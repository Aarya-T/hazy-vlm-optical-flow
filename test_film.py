import torch

from src.vlm_tokens.film import FiLM

# Dummy feature vector
feature = torch.randn(1, 128)

# Dummy haze token
token = torch.randn(1, 128)

film = FiLM()

output = film(feature, token)

print("Feature shape :", feature.shape)
print("Token shape   :", token.shape)
print("Output shape  :", output.shape)

print("\nFirst 10 values:")
print(output[0][:10])