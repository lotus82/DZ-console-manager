IS_ACTIVE = True
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

# Создать папку
def create_folder():
    pass

# Удалить (файл/папку)
def del_folder():
    pass

# Копировать (файл/папку)
def copy_file():
    pass

# Просмотр содержимого рабочей директории
def list_path():
    pass

# Посмотреть только папки
def list_folders():
    pass

# Посмотреть только файлы
def list_files():
    pass

# Просмотр информации об ОС
def info_os():
    pass

# Создатель программы
def info_owner():
    pass

# Играть в викторину
def game():
    pass

# Мой банковский счет
def bank():
    pass

# Смена рабочей директории
def change_path():
    pass

# Выход
def close_app():
    global IS_ACTIVE
    IS_ACTIVE = False

if __name__ == "__main__":
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
            list_folders()
        elif choice == '6':
            list_files()
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