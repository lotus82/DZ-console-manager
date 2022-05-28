import os
from saving import uploader
from saving import downloader

# пополнение счета
def score_up():
    global score
    try:
        score += int(input('Введите сумму пополнения: '))
        print('*' * 20 + '\nУспешное пополнение счента\n' + '*' * 20)
    except Exception as err:
        print('[ОШИБКА]', err)

# покупка
def buy():
    global score, history
    try:
        b = int(input('Введите сумму покупки (баланс: {0} рублей): '.format(score)))
        if score < b:
            print('*'*20 + '\nНедостаточно средств на счете\n' + '*'*20)
        else:
            name_buy = input('Введите название покупки: ')
            score -= b
            history.append({name_buy:b})
            print('*'*20 + '\nУспешная покупка\n' + '*'*20)
    except Exception as err:
        print('[ОШИБКА]', err)

# история покупок
def history_buy():
    global history
    s = '*'*10 + 'ИСТОРИЯ' + '*'*10 + '\n\n'
    for item in history:
        for k, v in item.items():
            s += str(k) + " --> " + str(v) + " рублей\n"
    s += '\n' + '*'*27
    print(s)

# выход из программы
def close_app():
    global opened, history
    uploader.save_history(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history.csv'), history)
    uploader.save_score(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'score.txt'), score)
    opened = False
    print('До свидания')

opened = True
score = 0
history = []

def start_bank():
    global opened, score, history
    history = downloader.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history.csv'))
    score = downloader.read_txt(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'score.txt'))
    opened = True
    while opened:
        print('='*8 + 'БАНК МЕНЮ' + '='*8)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('=' * 25)
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            score_up()
        elif choice == '2':
            buy()
        elif choice == '3':
            history_buy()
        elif choice == '4':
            close_app()
        else:
            print('Неверный пункт меню')