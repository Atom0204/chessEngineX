### utils.py — PGN parsing and board-to-tensor conversion

import chess.pgn
import numpy as np
import torch

def board_to_tensor(board):
    tensor = np.zeros(773, dtype=np.float32)
    for square, piece in board.piece_map().items():
        offset = piece.piece_type - 1 + (0 if piece.color == chess.WHITE else 6)
        tensor[square + offset * 64] = 1.0
    tensor[768] = int(board.turn)
    tensor[769] = int(board.has_kingside_castling_rights(chess.WHITE))
    tensor[770] = int(board.has_queenside_castling_rights(chess.WHITE))
    tensor[771] = int(board.has_kingside_castling_rights(chess.BLACK))
    tensor[772] = int(board.has_queenside_castling_rights(chess.BLACK))
    return tensor

def load_pgn_data(pgn_path, max_games=1000):
    X, y = [], []
    with open(pgn_path, "r", encoding="utf-8") as f:
        for _ in range(max_games):
            game = chess.pgn.read_game(f)
            if game is None:
                break
            result = game.headers.get("Result")
            if result == "1-0": score = 1
            elif result == "0-1": score = -1
            else: score = 0

            board = game.board()
            for move in game.mainline_moves():
                board.push(move)
                X.append(torch.tensor(board_to_tensor(board)))
                y.append(torch.tensor([score], dtype=torch.float32))
    return torch.stack(X), torch.stack(y)
