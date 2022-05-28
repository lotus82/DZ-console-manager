from saving import uploader
from saving import downloader
import os
import csv

def test_save_history():
    os.chdir(os.path.join('..', 'bank'))
    folder = os.getcwd()
    history = [{'гречка':80}, {'рис':60}, {'соль':20}]
    if os.path.exists('history_.csv'):
        os.remove('history_.csv')
    if os.path.exists('history.csv'):
        os.renames('history.csv', 'history_.csv')
    uploader.save_history('history.csv', history)
    assert 'history.csv' in os.listdir(folder) # сохранение файла
    history_temp = []
    with open('history.csv', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            history_temp.append({row[0]: row[1]})
    assert len(history_temp) == 3 # количество элементов истории
    assert 'гречка' in history_temp[0].keys() # кодировка
    os.remove('history.csv')
    os.renames('history_.csv', 'history.csv')

def test_save_score():
    os.chdir(os.path.join('..', 'bank'))
    folder = os.getcwd()
    score = 100
    if os.path.exists('score_.txt'):
        os.remove('score_.txt')
    if os.path.exists('score.txt'):
        os.renames('score.txt', 'score_.txt')
    uploader.save_score('score.txt', score)
    assert 'score.txt' in os.listdir(folder)  # сохранение файла
    score_temp = 0
    with open('score.txt', encoding='utf-8') as r_file:
        score_temp = int(r_file.readline())
    assert score_temp == 100  # счет
    os.remove('score.txt')
    os.renames('score_.txt', 'score.txt')

def test_save_listdir():
    os.chdir(os.path.join('..'))
    folder = os.getcwd()
    lst = os.listdir(folder)
    if os.path.exists('listdirectory_.txt'):
        os.remove('listdirectory_.txt')
    if os.path.exists('listdirectory.txt'):
        os.renames('listdirectory.txt', 'listdirectory_.txt')
    uploader.save_listdir('listdirectory.txt', lst, folder)
    uploader.save_listdir('listdirectory.txt', lst, folder) # еще раз вызываем, чтобы созданный файл тоже попал в список
    assert 'listdirectory.txt' in os.listdir(folder)  # сохранение файла
    str_folder = ''
    str_files = ''
    with open('listdirectory.txt', encoding='utf-8') as r_file:
        str_folder = r_file.readline()
        str_files = r_file.readline()
    assert 'folders: ' in str_folder  # формат содержимого
    assert 'files: ' in str_files  # формат содержимого
    assert 'listdirectory.txt' in str_files  # формат содержимого
    assert 'testing' in str_folder  # формат содержимого
    os.remove('listdirectory.txt')
    os.renames('listdirectory_.txt', 'listdirectory.txt')

def test_read_csv():
    os.chdir(os.path.join('..', 'bank'))
    history = [{'гречка': 80}, {'рис': 60}, {'соль': 20}]
    if os.path.exists('history_test.csv'):
        os.remove('history_test.csv')
    uploader.save_history('history_test.csv', history)
    history = downloader.read_csv('history.csv')
    assert isinstance(history, list) # тип
    assert len(history) == 3  # количество элементов истории
    assert 'гречка' in history[0].keys()  # кодировка

def test_read_txt():
    os.chdir(os.path.join('..', 'bank'))
    score = 100
    if os.path.exists('score_test.txt'):
        os.remove('score_test.txt')
    uploader.save_score('score.txt', score)
    score = downloader.read_txt('score.txt')
    assert score == 100  # счет
