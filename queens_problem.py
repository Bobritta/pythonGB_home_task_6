# Напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

QUEEN_COUNT = 8
queens_ccordinates = []
def show_possible_queen_moves(a, b):
    possible_queen_moves = []
    for i in range(1, 9):
        if i != b:
            possible_queen_moves.append([a, i])
        if i != a:
            possible_queen_moves.append([i, b])
    for i in range(1, 9):
        for j in range(1, 9):
            if abs(i - a) == abs(j - b) and a!=i:
                possible_queen_moves.append([i, j])
    return possible_queen_moves


def check_possibility(queens_coordinates):
    for i, queen in enumerate(queens_coordinates):
        for other_queen in queens_coordinates[i + 1:]:
            if other_queen in show_possible_queen_moves(queen[0], queen[1]):
                return False
    return True


def find_right_combinations():
    success_attempts = []
    def place_queens(current_queens):
        if len(current_queens) == QUEEN_COUNT:
            success_attempts.append(current_queens[:])
            return
        # Проверяем только одну клетку в каждом ряду, так как ферзи не могут находиться в одном ряду
        for col in range(1, 9):
            new_queen = [len(current_queens) + 1, col]
            if all(new_queen not in show_possible_queen_moves(q[0], q[1]) for q in current_queens):
                current_queens.append(new_queen)
                place_queens(current_queens)
                current_queens.pop()

    place_queens([])
    return success_attempts


if __name__ == "__main__":
    success_attempts = find_right_combinations()

    print(f"Найдено {len(success_attempts)} успешных комбинаций:")
    for attempt in success_attempts:
        print(attempt)