# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
Результат этого варианта: Найдено 4 успешных комбинаций через 1158456 попыток.
"""

from random import randint
import queens_problem


def make_attempt():
    attempt = []
    for i in range(1, 9):
        a = i
        b = randint(1, 8)
        attempt.append([a, b])
    return attempt


SUCCESS_COUNT = 4
success_attempts = 0
all_attampts = 0

list_of_suited_combinations = queens_problem.find_right_combinations()

while success_attempts < SUCCESS_COUNT:
    variation = make_attempt()
    if variation in list_of_suited_combinations:
        success_attempts +=1
    all_attampts+=1

print(f"Найдено {success_attempts} успешных комбинаций через {all_attampts} попыток.")

