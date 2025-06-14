import torch
import os
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

from utils import load_pgn_data
from net import ChessNet

# Select GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("CUDA Available:", torch.cuda.is_available())
print("Using:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")


class ChessDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

def train_model():
    os.makedirs("models", exist_ok=True)

    # Load PGN and preprocess
    X, y = load_pgn_data("../data/lichess_db_standard_rated_2015-09.pgn", max_games=4000)

    dataset = ChessDataset(X, y)
    loader = DataLoader(dataset, batch_size=64, shuffle=True, num_workers=2, pin_memory=True)

    model = ChessNet().to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    loss_fn = nn.MSELoss()

    for epoch in range(20):
        total_loss = 0
        for xb, yb in tqdm(loader, desc=f"Epoch {epoch+1}"):
            xb = xb.to(device).float()
            yb = yb.to(device).float()

            pred = model(xb)
            loss = loss_fn(pred, yb)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}: Loss = {total_loss:.4f}")

    torch.save(model.state_dict(), "models/trained_chessnet.pt")
    print("Model saved to models/trained_chessnet.pt")

if __name__ == "__main__":
    train_model()
