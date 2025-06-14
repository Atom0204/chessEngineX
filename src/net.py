import torch
import torch.nn as nn

class ChessNet(nn.Module):
    def __init__(self):
        super(ChessNet, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(773, 1024),
            nn.BatchNorm1d(1024),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(256, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.2),

            nn.Linear(64, 1),
            nn.Tanh()  # Outputs in range [-1, 1]
        )

    def forward(self, x):
        return self.model(x).squeeze(1)
