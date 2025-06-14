import chess
import torch
from net import ChessNet
from utils import board_to_tensor

# Set device: use GPU if available, else fallback to CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the trained neural network model
model = ChessNet().to(device)
model.load_state_dict(torch.load("models/trained_chessnet.pt", map_location=device))
model.eval()

def evaluate_board(board):
    tensor = torch.tensor(board_to_tensor(board), dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        value = model(tensor)
    return value.item()


def get_best_move(board, depth=1):
    """Selects the best move using NN evaluation. Depth can be extended for minimax later."""
    best_move = None
    is_white = board.turn
    best_value = -float('inf') if is_white else float('inf')

    for move in board.legal_moves:
        board.push(move)
        value = evaluate_board(board)
        board.pop()

        if is_white and value > best_value:
            best_value = value
            best_move = move
        elif not is_white and value < best_value:
            best_value = value
            best_move = move

    return best_move
