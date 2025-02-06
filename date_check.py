# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

from datetime import datetime as dt
from sys import argv


def check_date(date: str):
    if len(date.split(".")) == 3:
        try:
            _ = dt.strptime(date, '%d.%m.%Y')
            print("Дата существует")
        except:
            print("Дата не существует")
    else:
        print("Вероятно, дата введена в некорректном формате. "
              "Напишите число, затем '.', далее месяц, снова '.' и, наконец, год. Не используйте пробелы: ")



if __name__ == "__main__":
    if len(argv) > 1:
        user_date = argv[1]
        check_date(user_date)
        argv.clear()
        again = input("Проверить дату ещё раз? (да/нет): ")
        if again != str.lower("да"):
            exit()
    while True:
        user_date = input("Напишите число, затем '.', далее месяц, снова '.' и, наконец, год. Не используйте пробелы: ")
        check_date(user_date)
        again = input("Проверить дату ещё раз? (да/нет): ")
        if again != str.lower("да"):
            break
