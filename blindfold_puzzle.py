import sys
import requests
import chess

# Function to get the puzzle's FEN and turn from Lichess API
def get_puzzle_data(puzzle_id):
    url = f"https://lichess.org/api/puzzle/{puzzle_id}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        data = response.json()
        pgn = data['game']['pgn']
        puzzle_info = data['puzzle']
        solution = puzzle_info['solution']
        rating = puzzle_info['rating']
        plays = puzzle_info['plays']
        initial_ply = puzzle_info['initialPly']
        moves = pgn.split()
        turn = 'w' if len(moves) % 2 == 0 else 'b'  # Even moves means White's turn
        return pgn, initial_ply, turn, solution, rating, plays
    else:
        raise ValueError(f"Failed to retrieve puzzle data for ID {puzzle_id} with status code {response.status_code}")

# Function to play the moves from the PGN and reach the desired position
def get_final_board_from_pgn(pgn, initial_ply):
    board = chess.Board()  # Start from the initial chess position
    moves = pgn.split()
    for move in moves[:initial_ply + 1]:
        board.push_san(move)  # Play the move
    return board

# Function to get piece positions sorted by their value
def get_sorted_piece_positions(board, turn):
    # Define piece values
    piece_values = {
        'p': 1, 'P': 1,
        'n': 3, 'N': 3,
        'b': 3.5, 'B': 3.5,
        'r': 5, 'R': 5,
        'q': 9, 'Q': 9,
        'k': 10, 'K': 10
    }

    # Full piece names
    piece_names = {
        'p': 'Pawn', 'P': 'Pawn',
        'n': 'Knight', 'N': 'Knight',
        'b': 'Bishop', 'B': 'Bishop',
        'r': 'Rook', 'R': 'Rook',
        'q': 'Queen', 'Q': 'Queen',
        'k': 'King', 'K': 'King'
    }
    
    # Collect pieces with their positions and values, and whether it's their turn
    white_pieces = []
    black_pieces = []
    
    white_pawn_positions = []
    black_pawn_positions = []
    
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            square_name = chess.square_name(square)
            piece_symbol = piece.symbol()
            value = piece_values[piece_symbol]
            piece_name = piece_names[piece_symbol]
            
            if piece_symbol.isupper():  # White piece
                if piece_symbol == 'P':  # White Pawn
                    white_pawn_positions.append(square_name)
                else:
                    white_pieces.append((value, piece_name, square_name))
            else:  # Black piece
                if piece_symbol == 'p':  # Black Pawn
                    black_pawn_positions.append(square_name)
                else:
                    black_pieces.append((value, piece_name, square_name))

    # Sort the pawns from left to right (by their file)
    white_pawn_positions.sort()
    black_pawn_positions.sort()

    # Sort pieces by value (highest first)
    white_pieces.sort(reverse=True, key=lambda x: x[0])
    black_pieces.sort(reverse=True, key=lambda x: x[0])

    # Prioritize the pieces of the player whose turn it is next
    if turn == 'w':  # White's turn
        return white_pieces, white_pawn_positions, black_pieces, black_pawn_positions
    else:  # Black's turn
        return black_pieces, black_pawn_positions, white_pieces, white_pawn_positions

def play_puzzle_interactively(solution, rating, plays):
    for i, move in enumerate(solution):
        if i % 2 == 0:  # Player's turn (even indices)
            my_move = input("Your move: ").strip()
            if my_move == move:
                print("Correct!")
                print("#" * 22)
                if i == len(solution) - 1:  # Last move in the solution
                    print(f"SUCCESS! You solved a {rating} rating puzzle played {plays} times perfectly!")
                    return
            else:
                print(f"Wrong! GAME OVER! You got a {rating} rating puzzle played {plays} times wrong...")
                if input("Do you want to see the solution? (yes/no): ").strip().lower() in {'yes', 'y'}:
                    print("Solution:", " ".join(solution))
                return
        else:  # Opponent's turn (odd indices)
            print(f"Opponent's move: {move}")
            print("#" * 22)

# Main function to get and display sorted piece positions and whose turn it is
def main(puzzle_id):
    try:
        pgn, initial_ply, turn, solution, rating, plays = get_puzzle_data(puzzle_id)
        board = get_final_board_from_pgn(pgn, initial_ply)
        
        # Get sorted piece positions, with current player's pieces first
        winner_pieces, winner_pawn_positions, loser_pieces, loser_pawn_positions = get_sorted_piece_positions(board, turn)
        
        # Inform whose turn it is
        current_player = "White" if turn == 'w' else "Black"
        other_player = "Black" if turn == 'w' else "White"
        print(f"{current_player} to move next.\n")
        
        # Display White pieces
        print(f"{current_player} pieces:")
        print("-----------")
        # Show pieces
        for _, piece, square in winner_pieces:
            print(f"{piece} on {square}.")
        # Show pawns from left to right
        for pawn in winner_pawn_positions:
            print(f"Pawn on {pawn}.")
        
        # Display Black pieces
        print(f"\n{other_player} pieces:")
        print("-----------")
        # Show pieces
        for _, piece, square in loser_pieces:
            print(f"{piece} on {square}.")
        # Show pawns from left to right
        for pawn in loser_pawn_positions:
            print(f"Pawn on {pawn}.")

        print("\nLet's solve the puzzle!")
        play_puzzle_interactively(solution, rating, plays)
    
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    puzzle_id = sys.argv[1]
    main(puzzle_id)
