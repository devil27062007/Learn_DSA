def create_board():
    return [
        ["r","n","b","q","k","b","n","r"],
        ["p","p","p","p","p","p","p","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["P","P","P","P","P","P","P","P"],
        ["R","N","B","Q","K","B","N","R"]
    ]

def print_board(board):
    print("\n  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print(8 - i)
    print("  a b c d e f g h\n")

def parse_move(move):
    col_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    try:
        sc = col_map[move[0]]
        sr = 8 - int(move[1])
        ec = col_map[move[2]]
        er = 8 - int(move[3])
        return sr, sc, er, ec
    except:
        return None

def is_valid_move(board, sr, sc, er, ec, player):
    piece = board[sr][sc]
    target = board[er][ec]

    if piece == ".":
        return False

    # White player uses uppercase pawn
    if player == "white":
        if piece != "P":
            return False

        # one step forward
        if er == sr - 1 and ec == sc and target == ".":
            return True

        # two steps from starting position
        if sr == 6 and er == 4 and ec == sc and board[5][sc] == "." and target == ".":
            return True

        # diagonal capture
        if er == sr - 1 and abs(ec - sc) == 1 and target.islower():
            return True

    # Black player uses lowercase pawn
    elif player == "black":
        if piece != "p":
            return False

        # one step forward
        if er == sr + 1 and ec == sc and target == ".":
            return True

        # two steps from starting position
        if sr == 1 and er == 3 and ec == sc and board[2][sc] == "." and target == ".":
            return True

        # diagonal capture
        if er == sr + 1 and abs(ec - sc) == 1 and target.isupper():
            return True

    return False

def make_move(board, sr, sc, er, ec):
    board[er][ec] = board[sr][sc]
    board[sr][sc] = "."

def count_pawns(board, pawn):
    count = 0
    for row in board:
        count += row.count(pawn)
    return count

def play_chess():
    board = create_board()
    player = "white"

    while True:
        print_board(board)
        print(player, "turn (example: e2e4): ", end="")
        move = input().strip()

        if move == "exit":
            break

        parsed = parse_move(move)
        if not parsed:
            print("Invalid input!")
            continue

        sr, sc, er, ec = parsed

        if not is_valid_move(board, sr, sc, er, ec, player):
            print("Invalid pawn move!")
            continue

        make_move(board, sr, sc, er, ec)

        # win check
        if count_pawns(board, "p") == 0:
            print("White wins!")
            break
        if count_pawns(board, "P") == 0:
            print("Black wins!")
            break

        player = "black" if player == "white" else "white"

# Run game
play_chess()