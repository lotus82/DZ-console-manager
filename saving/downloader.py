import csv
import os

def read_csv(path):
    if os.path.exists(path):
        history = []
        with open(path, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                history.append({row[0]: row[1]})
    else:
        print('[ERROR]: отсутствует файл ', path)
    return history

def read_txt(path):
    score = 0
    if os.path.exists(path):

        with open(path, encoding='utf-8') as r_file:
            score = int(r_file.readline())
    else:
        print('[ERROR]: отсутствует файл ', path)
    return  score