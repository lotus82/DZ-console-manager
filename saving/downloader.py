import csv
import os

# чтение истории покупок
# использование генератора списков
# обработка исключений
def read_csv(path):
    try:
        history = []
        if os.path.exists(path):
            with open(path, encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=";")
                history = [{row[0]: row[1]} for row in file_reader]
        else:
            print('[ERROR]: отсутствует файл ', path)
    except Exception as err:
        print('[ERROR]: ошибка чтения истории покупок: ', err)
    finally:
        return history

# чтение баланса
# обработка исключений
def read_txt(path):
    try:
        score = 0
        if os.path.exists(path):
            with open(path, encoding='utf-8') as r_file:
                score = int(r_file.readline())
        else:
            print('[ERROR]: отсутствует файл ', path)
    except Exception as err:
        print('[ERROR]: ошибка чтения баланса: ', err)
    finally:
        return  score