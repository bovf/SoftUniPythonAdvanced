def read_matrix():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        matrix.append([x for x in input()])
    return matrix


def find_all_knights(matrix):
    knight_matrix = []

    for matrix_list in range(len(matrix)):
        for square in range(len(matrix[matrix_list])):
            if matrix[matrix_list][square] == "K":
                knight_matrix.append((matrix_list, square))
    return knight_matrix


def knight_are_attacking_each_other(matrix):
    knight_positions = find_all_knights(matrix)
    for row, col in knight_positions:
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1)
        ]
        for positions in positions_to_check:
            pos_row, pos_col = positions
            if not (0 <= pos_row <= len(matrix) - 1):
                continue
            if not (0 <= pos_col <= len(matrix) - 1):
                continue
            if matrix[pos_row][pos_col] == "K":
                return True
    return False


def calculate_aggression(matrix, knight_positions):
    aggression_score = {}
    for position in knight_positions:
        row, col = position
        positions_to_check = [
            (row - 2, col + 1),
            (row - 1, col + 2),
            (row + 1, col + 2),
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row - 2, col - 1)]
        attacked_count = 0
        for attacked_row, attacked_col in positions_to_check:
            if not (0 <= attacked_row <= len(matrix) - 1):
                continue
            if not (0 <= attacked_col <= len(matrix) - 1):
                continue
            if matrix[attacked_row][attacked_col] == "K":
                attacked_count += 1
        aggression_score[(row, col)] = attacked_count
    return aggression_score


def find_max_aggression(aggression_scores):
    max_so_far = None
    max_pos = None
    for pos, aggression in aggression_scores.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos
    return max_pos


def main():
    matrix = read_matrix()
    knights_removed = 0
    while knight_are_attacking_each_other(matrix):
        knight_positions = find_all_knights(matrix)
        aggression_scores = calculate_aggression(matrix, knight_positions)
        row, col = find_max_aggression(aggression_scores)
        matrix[row][col] = "0"
        knights_removed += 1
    return knights_removed


print(main())
