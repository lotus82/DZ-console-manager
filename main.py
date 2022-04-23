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
def main_menu(menu_dict):
    count = 1
    s_menu = ""
    for k,v in menu_dict.items():
        if count % 2 == 0:
            s_menu = s_menu + k.rjust(2, " ") + " - " + v.ljust(39, " ") + " ||\n"
        else:
            s_menu = s_menu + "|| " + k.rjust(2, " ") + " - " + v.ljust(25, " ") + " || "
        count+=1
    return "="*40 + "МЕНЮ" + "="*40 + "\n" + s_menu + "=" * 84

# 1 - Создать папку
def create_folder(dir_name):
    try:
        os.mkdir(dir_name)
    except OSError as err:
        return("Ошибка создания директории: %s" % dir_name, ":", err)
    else:
        return("-" * 84 + "\nСоздана директория: %s " % dir_name + "\n" + "-"*84)

# 2 - Удалить (файл/папку)
def del_folder(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            try:
                os.remove(path)
                return("-" * 84 + "\nУдален файл: %s " % path + "\n" + "-" * 84)
            except Exception as err:
                return("Ошибка удаления файла: %s" % path, ":", err)
        else:
            try:
                if input("Удалить папку вместе со всем содержимым, да?") in ["да", "Да", "ДА", "yes", "Yes", "YES", "y", "Y", "ok", "Ok", "OK", "д", "Д"]:
                    shutil.rmtree(path)
                    return("-" * 84 + "\nУдалена папка: %s " % path + " со всем ее содержимым\n" + "-" * 84)
                else:
                    return("-" * 84 + "\nУдаление отменено\n" + "-" * 84)
            except Exception as err:
                return("Ошибка удаления папки: %s" % path, ":", err)
    else:
        return("-" * 84 + "\nТакого файла или папки здесь нет: %s " % path + "\n" + "-" * 84)

# 3 - Копировать (файл/папку)
def copy_file(inp, outp):
    if os.path.exists(inp):
        if os.path.isfile(inp):
            try:
                shutil.copyfile(inp, outp)
                return("-" * 84 + "\nСкопирован файл: %s " % inp + " в: %s " % outp + "\n" + "-" * 84)
            except Exception as err:
                return("Ошибка копирования файла: %s " % inp + " в: %s " % outp, ":", err)
        else:
            try:
                shutil.copytree(inp, outp)
                return("-" * 84 + "\nСкопирована папка: %s " % inp + " в: %s " % outp + "\n" + "-" * 84)
            except Exception as err:
                return("Ошибка копирования папки: %s " % inp + " в %s " % outp, ":", err)
    else:
        return("-" * 84 + "\nТакого файла или папки здесь нет: %s " % inp + "\n" + "-" * 84)

# 4,5,6 - Просмотр содержимого рабочей директории
def list_path(param="all"):
    try:
        content = os.listdir(CUR_DIR)
        s = ""
        for item in content:
            if param == "files":
                if os.path.isfile(os.path.join(CUR_DIR,item)):
                    s += item + "\n"
            if param == "folders":
                if not os.path.isfile(os.path.join(CUR_DIR,item)):
                    s += item + "\n"
            if param == "all":
                s += item + "\n"
        return ("-" * 84 + "\n" + s + "-" * 84)
    except Exception as err:
        return("Ошибка просмотра содержимого рабочей директории: %s " % CUR_DIR, ":", err)

# 7 - Просмотр информации об ОС
def info_os():
    try:
        info_dict = {
            "Имя пользователя" : getpass.getuser(),
            "IP-адрес системы" : socket.gethostbyname(socket.getfqdn()),
            "MAC адрес" : get_mac(),
            "Название операционной системы" : platform.uname()
        }
        s = "-" * 84 + "\n"
        for k,v in info_dict.items():
            s += k + " --> " + v + "\n"
        return(s + "-" * 84)
    except Exception as err:
        return("Ошибка получения информации: ", err)

# 8 - Создатель программы
def info_owner(OWNER):
    return("-" * 84 + "\nСоздатель программы: " + OWNER + "-" * 84)

# 9 - Играть в викторину
def game():
    vic.start_game()

# 10 - Мой банковский счет
def bank():
    b.start_bank()

# 11 - Смена рабочей директории
def change_path(new_path):
    global CUR_DIR
    try:
        os.chdir(new_path)
        CUR_DIR = new_path
        return "Рабочая директория сменена на: " + new_path
    except Exception as err:
        return "Ошибка смены рабочей директории на : %s" % new_path + ":" + err

# 12 - Выход
def close_app():
    global IS_ACTIVE
    IS_ACTIVE = False

# Запуск приложения
def run_app():
    while IS_ACTIVE:
        print(main_menu(menu_dict))
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print(create_folder(input("Введите имя папки: ")))
        elif choice == '2':
            print(del_folder(input("Введите имя папки или файла: ")))
        elif choice == '3':
            print(copy_file(input("Введите что копировать: "), input("Введите куда копировать: ")))
        elif choice == '4':
            print(list_path())
        elif choice == '5':
            print(list_path("folders"))
        elif choice == '6':
            print(list_path("files"))
        elif choice == '7':
            print(info_os())
        elif choice == '8':
            print(info_owner(OWNER))
        elif choice == '9':
            game()
        elif choice == '10':
            bank()
        elif choice == '11':
            print(change_path(input("Сменить рабочую директорию (" + CUR_DIR + "). Введите новый путь: ")))
        elif choice == '12':
            close_app()
        else:
            print('Неверный пункт меню')
    print("До свидания")
    exit()

if __name__ == "__main__":
    run_app()