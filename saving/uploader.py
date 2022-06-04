import csv
import os.path

# сохранение истории покупок в файл
# использование генератора списков
# вложенные циклы, где внутренний цикл идет по результату внешнего цикла
# обработка исключений
def save_history(path, history_dict):
    try:
        with open(path, mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            [file_writer.writerow([k, v]) for item in history_dict for k, v in item.items()]
    except Exception as err:
        print('[ERROR]: ошибка сохранения истории покупок: ', err)

# сохранение счета в файл
# обработка исключений
def save_score(path, score):
    try:
        with open(path, mode="w", encoding='utf-8') as w_file:
            w_file.write(str(score))
    except Exception as err:
        print('[ERROR]: ошибка сохранения счета: ', err)

# сохранение содержимого директории в файл
# использование генератора списков
# обработка исключений
def save_listdir(path, lst, cur_dir):
    try:
        folders = [item for item in lst if os.path.isfile(os.path.join(cur_dir, item))]
        files = [item for item in lst if not os.path.isfile(os.path.join(cur_dir, item))]
        with open(path, mode="w", encoding='utf-8') as w_file:
            w_file.write('folders: ')
            w_file.write(', '.join(folders))
            w_file.write('\nfiles: ')
            w_file.write(', '.join(files))
        return True
    except Exception as err:
        print('[ERROR]: ошибка сохранения содержимого рабочей директории: ', err)
        return False