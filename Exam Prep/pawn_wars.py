def find_piece(piece, board):
    for row_i in range(len(board)):
        for col_i in range(len(board[row_i])):
            if board[row_i][col_i] == piece:
                return [row_i, col_i]


def can_piece_capture(attacking_piece, defending_piece):
    a_row = attacking_piece[0]
    a_col = attacking_piece[1]
    d_row = defending_piece[0]
    d_col = defending_piece[1]

    if a_row - 1 >= 0 and a_col - 1 >= 0:
        if a_row - 1 == d_row and a_col - 1 == d_col:
            return [a_row - 1, a_col - 1]
    if a_row - 1 >= 0 and a_col + 1 < 8:
        if a_row - 1 == d_row and a_col + 1 == d_col:
            return [a_row - 1, a_col + 1]
    if a_row + 1 < 8 and a_col - 1 >= 0:
        if a_row + 1 == d_row and a_col - 1 == d_col:
            return [a_row + 1, a_col - 1]
    if a_row + 1 < 8 and a_col + 1 < 8:
        if a_row + 1 == d_row and a_col + 1 == d_col:
            return [a_row + 1, a_col + 1]


matrix = []
for i in range(8):
    matrix.append(input().split())

board_cols = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

board_rows = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}

white_pawn_pos = find_piece("w", matrix)
black_pawn_pos = find_piece("b", matrix)

for i in range(8):
    capture = can_piece_capture(white_pawn_pos, black_pawn_pos)
    if capture:
        capture_pos = board_cols[capture[1]], board_rows[capture[0]]
        print(f"Game over! White win, capture on {''.join([str(x) for x in list(capture_pos)])}.")
        break

    white_pawn_pos[0] -= 1
    if white_pawn_pos[0] == 0:
        queen_pos = board_cols[white_pawn_pos[1]], board_rows[white_pawn_pos[0]]
        print(f"Game over! White pawn is promoted to a queen at {''.join([str(x) for x in list(queen_pos)])}.")
        break
    capture = can_piece_capture(black_pawn_pos, white_pawn_pos)
    if capture:
        capture_pos = board_cols[capture[1]], board_rows[capture[0]]
        print(f"Game over! Black win, capture on {''.join([str(x) for x in list(capture_pos)])}.")
        break

    black_pawn_pos[0] += 1
    if black_pawn_pos[0] == 7:
        queen_pos = board_cols[black_pawn_pos[1]], board_rows[black_pawn_pos[0]]
        print(f"Game over! Black pawn is promoted to a queen at {''.join([str(x) for x in list(queen_pos)])}.")
        break
