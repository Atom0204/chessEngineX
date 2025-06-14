import pygame
import chess
from engine import get_best_move

# Constants
WIDTH, HEIGHT = 512, 512
SQ_SIZE = WIDTH // 8

def load_images():
    pieces = {
        'P': 'wP', 'R': 'wR', 'N': 'wN', 'B': 'wB', 'Q': 'wQ', 'K': 'wK',
        'p': 'bP', 'r': 'bR', 'n': 'bN', 'b': 'bB', 'q': 'bQ', 'k': 'bK',
    }
    images = {}
    for symbol, filename in pieces.items():
        path = f"images/{filename}.png"
        images[symbol] = pygame.transform.scale(
            pygame.image.load(path), (SQ_SIZE, SQ_SIZE)
        )
    return images

def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board, images):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            piece_img = images[piece.symbol()]
            screen.blit(piece_img, pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def get_clicked_square(pos):
    x, y = pos
    col = x // SQ_SIZE
    row = 7 - (y // SQ_SIZE)
    return chess.square(col, row)

def animate_move(screen, board, move, images):
    frames_per_square = 5
    d_row = chess.square_rank(move.to_square) - chess.square_rank(move.from_square)
    d_col = chess.square_file(move.to_square) - chess.square_file(move.from_square)

    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square
    if frame_count == 0:
        return

    from_row = 7 - chess.square_rank(move.from_square)
    from_col = chess.square_file(move.from_square)
    to_row = 7 - chess.square_rank(move.to_square)
    to_col = chess.square_file(move.to_square)

    piece = board.piece_at(move.from_square)
    image = images[piece.symbol()]
    clock = pygame.time.Clock()

    for frame in range(frame_count + 1):
        draw_board(screen)
        temp_board = board.copy()
        temp_board.remove_piece_at(move.from_square)  # Hide moving piece
        draw_pieces(screen, temp_board, images)

        dx = (to_col - from_col) * SQ_SIZE * frame / frame_count
        dy = (to_row - from_row) * SQ_SIZE * frame / frame_count
        x = from_col * SQ_SIZE + dx
        y = from_row * SQ_SIZE + dy
        screen.blit(image, pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))
        pygame.display.flip()
        clock.tick(60)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()
    board = chess.Board()
    images = load_images()
    selected_square = None
    player_color = chess.WHITE  # You play white

    running = True
    while running:
        draw_board(screen)
        draw_pieces(screen, board, images)
        pygame.display.flip()

        if board.turn != player_color and not board.is_game_over():
            move = get_best_move(board)
            if move:
                animate_move(screen, board, move, images)
                board.push(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == player_color:
                square = get_clicked_square(pygame.mouse.get_pos())
                if selected_square is None:
                    piece = board.piece_at(square)
                    if piece and piece.color == player_color:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        animate_move(screen, board, move, images)
                        board.push(move)
                    selected_square = None

        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
