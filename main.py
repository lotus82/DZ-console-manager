import os
import shutil
import getpass
import socket
from uuid import getnode as get_mac
import platform
import victorina.victorina as vic
import bank.bank as b

IS_ACTIVE = True
OWNER = "Дмитрий Сухов"
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
menu_dict = {
    '1':'Создать папку',
    '2':'Удалить (файл/папку)',
    '3':'Копировать (файл/папку)',
    '4':'Просмотр содержимого рабочей директории',
    '5':'Посмотреть только папки',
    '6':'Посмотреть только файлы',
    '7':'Просмотр информации об ОС',
    '8':'Создатель программы',
    '9':'Играть в викторину',
    '10':'Мой банковский счет',
    '11':'Смена рабочей директории',
    '12':'Выход'
}

# Вывод главного меню
def main_menu():
    print("="*40 + "МЕНЮ" + "="*40)
    count = 1
    s = ""
    for k,v in menu_dict.items():
        if count % 2 == 0:
            s = s + k.rjust(2, " ") + " - " + v.ljust(39, " ") + " || "
            print(s)
            s = ""
        else:
            s = s + "|| " + k.rjust(2, " ") + " - " + v.ljust(25, " ") + " || "
        count+=1
    print("=" * 84)

# 1 - Создать папку
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

# 4,5,6 - Просмотр содержимого рабочей директории
def list_path(param="all"):
    global CUR_DIR
    try:
        content = os.listdir(CUR_DIR)
        print("-" * 84)
        for item in content:
            if param == "files":
                if os.path.isfile(os.path.join(CUR_DIR,item)):
                    print(item)
            if param == "folders":
                if not os.path.isfile(os.path.join(CUR_DIR,item)):
                    print(item)
            if param == "all":
                print(item)
        print("-" * 84)
    except Exception as err:
        print("Ошибка просмотра содержимого рабочей директории: %s " % CUR_DIR, ":", err)

# 7 - Просмотр информации об ОС
def info_os():
    try:
        info_dict = {
            "Имя пользователя" : getpass.getuser(),
            "IP-адрес системы" : socket.gethostbyname(socket.getfqdn()),
            "MAC адрес" : get_mac(),
            "Название операционной системы" : platform.uname()
        }
        print("-" * 84 )
        for k,v in info_dict.items():
            print(k + " --> ", v)
        print("-" * 84)
    except Exception as err:
        print("Ошибка получения информации: ", err)

# 8 - Создатель программы
def info_owner():
    global OWNER
    print("-" * 84)
    print("Создатель программы: ", OWNER)
    print("-" * 84)

# 9 - Играть в викторину
def game():
    vic.start_game()

# 10 - Мой банковский счет
def bank():
    b.start_bank()

# 11 - Смена рабочей директории
def change_path():
    global CUR_DIR
    new_path = input("Сменить рабочую директорию. Введите новый путь: ")
    try:
        os.chdir(new_path)
        CUR_DIR = new_path
    except Exception as err:
        print("Ошибка смены рабочей директории на : %s" % new_path, ":", err)

# 12 - Выход
def close_app():
    global IS_ACTIVE
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
            list_path()
        elif choice == '5':
            list_path("folders")
        elif choice == '6':
            list_path("files")
        elif choice == '7':
            info_os()
        elif choice == '8':
            info_owner()
        elif choice == '9':
            game()
        elif choice == '10':
            bank()
        elif choice == '11':
            change_path()
        elif choice == '12':
            close_app()
        else:
            print('Неверный пункт меню')
    print("До свидания")
    exit()

if __name__ == "__main__":
    run_app()