from loto.player import Player
from loto.bag import Bag

player1 = None # вы-игрок
opponents = None # список игроков-соперников
bag = None # мешок
barrel = None # номер на новом бочонке
flag_game = False

# декоратор для добавления рамки карточки
def add_frame(func):
    def wrap(param1, param2):
        print(str(param2).ljust(46, ' '))
        print("=" * 46)
        result = func(param1, param2)
        print("=" * 46 + '\n')
        return result
    return wrap

@add_frame
def print_card(card, name):
    print(card)

# вывод меню игры
def edit_menu():
    print('=' * 16 + 'МЕНЮ ИГРЫ ЛОТО' + '=' * 16)
    print('1. Новая игра'.ljust(20,' '), '2. Продолжить игру'.ljust(20,' '), '3. Выход из игры'.ljust(20,' '))
    print('=' * 46)
    choice = input('Выберите пункт меню: ')
    new_game() if choice == '1' else resume_game() if choice == '2' else exit_game() if choice == '3' else print(
        'Неверный пункт меню')

# новая игра
def new_game():
    global count_players, player1, opponents, bag, flag_game, barrel
    started = False
    opponents = []
    your_name = input('Введите Ваше имя: ')
    while not started:
        count_players = input(your_name + ', введите количество игроков (вместе с Вами): ')
        if count_players.isdigit():
            if int(count_players) > 1:
                flag_type = False
                while not flag_type:
                    your_type = input(your_name + ', выберите Ваш (Player-1) тип игрока (man или comp): ')
                    if your_type in ['man','comp']:
                        flag_type = True
                    else:
                        print('Нужно ввести man или comp')
                player1 = Player(your_type, your_name)

                for i in range(2, int(count_players) + 1, 1):
                    flag_type = False
                    while not flag_type:
                        opponent_type = input(your_name + ', выберите тип игрока для Player-' + str(i) + ' (man или comp): ')
                        if opponent_type in ['man', 'comp']:
                            flag_type = True
                        else:
                            print('Нужно ввести man или comp')
                    opponents.append(Player(opponent_type, 'Player-' + str(i)))
                print('\n')
                bag = Bag()
                started = True
            else:
                print('Нужно ввести положительное число (большее чем 1)!')
        else:
            print('Нужно ввести число!')
    flag_game = True
    while flag_game:
        # достаем бочонок
        barrel = bag.get_barrel()
        print('#'*46 + '\n' + 'Новый бочонок: "' + str(barrel) + '" (осталось ' + str(bag.count)  + ')' + '\n' + '#'*46 + '\n')
        # отображение карточек
        if not player1.lost:
            print_card(player1.card.str_card, 'Ваша карточка (' + player1.name + ' - ' + player1.owner + ')')
        for player in opponents:
            print_card(player.card.str_card, 'Карточка игрока Player-' + player.name + ' (' + player.owner + ')')
        # ваш ход
        if not player1.lost:
            p1_move = player1.move(barrel)
            if p1_move == 'menu':
                edit_menu()
            elif p1_move == 'win':
                print('Игрок ' + player1.name + ' победил!!!!!')
                exit_game()
        # ходы игроков-соперников
        for player in opponents:
            p_move = player.move(barrel)
            if p_move == 'menu':
                edit_menu()
            elif p_move == 'win':
                print('$'*46 + '\nИгрок ' + player.name + ' победил!!!!!\n' + '$'*46)
                exit_game()
        # исключаем проигравшего игрока-соперника
        for i in range(len(opponents)):
            if opponents[i].lost == True:
                del(opponents[i])
                break
        # завершение игры по количеству игроков
        if (len(opponents) <= 1 and player1.lost == True) or (len(opponents) < 1 and player1.lost == False):
            print('Остался только один игрок!')
            exit_game()

# продолжить игру
def resume_game():
    print('Продолжаем игру')

# выход из игры
def exit_game():
    global flag_game
    print('Завершаем игру')
    flag_game = False

# запуск игры
def start_loto():
    new_game()
