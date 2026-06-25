import torch
import torch.nn as nn


class FiLM(nn.Module):
    """
    Feature-wise Linear Modulation (FiLM)

    Computes:
        gamma = f(haze_token)
        beta  = g(haze_token)

    and applies

        output = gamma * feature + beta
    """

    def __init__(self,
                 token_dim=128,
                 feature_dim=128):
        super().__init__()

        self.gamma = nn.Linear(token_dim, feature_dim)
        self.beta = nn.Linear(token_dim, feature_dim)

    def forward(self, feature, haze_token):

        gamma = self.gamma(haze_token)
        beta = self.beta(haze_token)

        output = gamma * feature + beta

        return output