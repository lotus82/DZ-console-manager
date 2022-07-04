import os
import shutil
import getpass
import socket
from uuid import getnode as get_mac
import platform
import victorina.victorina as vic
import loto.loto as l
import bank.bank as b
from saving import uploader


IS_ACTIVE = True
OWNER = "Дмитрий Сухов"
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
menu_dict = {
    '1':'Создать папку',
    '2':'Удалить (файл/папку)',
    '3':'Копировать (файл/папку)',
    '4':'Просмотр содержимого рабочей директории',
    '5':'Сохранить содержимое рабочей директории в файл',
    '6':'Посмотреть только папки',
    '7':'Посмотреть только файлы',
    '8':'Просмотр информации об ОС',
    '9':'Создатель программы',
    '10':'Играть в викторину',
    '11':'Играть в лото',
    '12':'Мой банковский счет',
    '13':'Смена рабочей директории',
    '14':'Выход'
}

# декоратор для добавления рамки
def add_frame(func):
    def wrap(param):
        print("+" * 84)
        result = func(param)
        print("+" * 84)
        return result
    return wrap

# Вывод главного меню
def main_menu():
    print("="*50 + "МЕНЮ" + "="*50)
    count = 1
    s = ""
    for k,v in menu_dict.items():
        if count % 2 == 0:
            s = s + k.rjust(2, " ") + " - " + v.ljust(39, " ") + " || "
            print(s)
            s = ""
        else:
            s = s + "|| " + k.rjust(2, " ") + " - " + v.ljust(46, " ") + " || "
        count+=1
    print("=" * 104)

# 1 - Создать  папку
def create_folder():
    try:
        dir_name = input("Введите имя папки: ")
        os.mkdir(dir_name)
    except OSError as err:
        print("Ошибка создания директории: %s" % dir_name, ":", err)
    else:
        print("-" * 84 + "\nСоздана директория: %s " % dir_name + "\n" + "-"*84)

# 2 - Удалить (файл/папку)
def del_folder():
    path = input("Введите имя папки или файла: ")
    if os.path.exists(path):
        if os.path.isfile(path):
            try:
                os.remove(path)
                print("-" * 84 + "\nУдален файл: %s " % path + "\n" + "-" * 84)
            except Exception as err:
                print("Ошибка удаления файла: %s" % path, ":", err)
        else:
            try:
                if input("Удалить папку вместе со всем содержимым, да?") in ["да", "Да", "ДА", "yes", "Yes", "YES", "y", "Y", "ok", "Ok", "OK", "д", "Д"]:
                    shutil.rmtree(path)
                    print("-" * 84 + "\nУдалена папка: %s " % path + " со всем ее содержимым\n" + "-" * 84)
                else:
                    print("-" * 84 + "\nУдаление отменено\n" + "-" * 84)
            except Exception as err:
                print("Ошибка удаления папки: %s" % path, ":", err)
    else:
        print("-" * 84 + "\nТакого файла или папки здесь нет: %s " % path + "\n" + "-" * 84)

# 3 - Копировать (файл/папку)
def copy_file():
    inp = input("Введите что копировать: ")
    outp = input("Введите куда копировать: ")
    if os.path.exists(inp):
        if os.path.isfile(inp):
            try:
                shutil.copyfile(inp, outp)
                print("-" * 84 + "\nСкопирован файл: %s " % inp + " в: %s " % outp + "\n" + "-" * 84)
            except Exception as err:
                print("Ошибка копирования файла: %s " % inp + " в: %s " % outp, ":", err)
        else:
            try:
                shutil.copytree(inp, outp)
                print("-" * 84 + "\nСкопирована папка: %s " % inp + " в: %s " % outp + "\n" + "-" * 84)
            except Exception as err:
                print("Ошибка копирования папки: %s " % inp + " в %s " % outp, ":", err)
    else:
        print("-" * 84 + "\nТакого файла или папки здесь нет: %s " % inp + "\n" + "-" * 84)

# 5 - Сохранение содержимого рабочей директории в файл
def save_list_dir():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'listdirectory.txt')
    lst = os.listdir(CUR_DIR)
    if uploader.save_listdir(path, lst, CUR_DIR):
        print('Успешное сохранение содержимого рабочей директории в listdirectory.txt')

# 4,6,7 - Просмотр содержимого рабочей директории
@add_frame
def list_path(param):
    global CUR_DIR
    try:
        content = os.listdir(CUR_DIR)
        for item in content:
            if param == "files":
                if os.path.isfile(os.path.join(CUR_DIR,item)):
                    print(item)
            if param == "folders":
                if not os.path.isfile(os.path.join(CUR_DIR,item)):
                    print(item)
            if param == "all":
                print(item)
    except Exception as err:
        print("Ошибка просмотра содержимого рабочей директории: %s " % CUR_DIR, ":", err)

# 8 - Просмотр информации об ОС
@add_frame
def info_os():
    try:
        info_dict = {
            "Имя пользователя" : getpass.getuser(),
            "IP-адрес системы" : socket.gethostbyname(socket.getfqdn()),
            "MAC адрес" : get_mac(),
            "Название операционной системы" : platform.uname()
        }
        for k,v in info_dict.items():
            print(k + " --> ", v)
    except Exception as err:
        print("Ошибка получения информации: ", err)

# 9 - Создатель программы
@add_frame
def info_owner():
    global OWNER
    print("Создатель программы: ", OWNER)

# 10 - Играть в викторину
def game():
    vic.start_game()

# 11 - Играть в лото
def loto():
    l.start_loto()

# 12 - Мой банковский счет
def bank():
    b.start_bank()

# 13 - Смена рабочей директории
def change_path():
    global CUR_DIR
    new_path = input("Сменить рабочую директорию. Введите новый путь: ")
    try:
        os.chdir(new_path)
        CUR_DIR = new_path
    except Exception as err:
        print("Ошибка смены рабочей директории на : %s" % new_path, ":", err)

# 14 - Выход
def close_app():
    global IS_ACTIVE, history
    IS_ACTIVE = False

# Запуск приложения
def run_app():
    global  IS_ACTIVE
    while IS_ACTIVE:
        main_menu()
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            create_folder()
        elif choice == '2':
            del_folder()
        elif choice == '3':
            copy_file()
        elif choice == '4':
            list_path("all")
        elif choice == '5':
            save_list_dir()
        elif choice == '6':
            list_path("folders")
        elif choice == '7':
            list_path("files")
        elif choice == '8':
            info_os()
        elif choice == '9':
            info_owner()
        elif choice == '10':
            game()
        elif choice == '11':
            loto()
        elif choice == '12':
            bank()
        elif choice == '13':
            change_path()
        elif choice == '14':
            close_app()
        else:
            print('Неверный пункт меню')
    print("До свидания")
    exit()

if __name__ == "__main__":
    run_app()