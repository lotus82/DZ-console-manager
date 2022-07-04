from loto.card import Card
import time

class Player():
    '''
    params:
        owner - кто играет, человек или компьютер ('man' | 'comp')
        name - имя игрока
        card - карточка игрока
        lost - проигрыш игрока

    methods:
        move - ход игрока
        cross_number - игрок зачеркнул число
        pass_move - игрок пропускает ход
        lost_move - игрок проиграл
    '''

    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.card = Card()
        self.lost = False

    def cross_number(self, barrel):
        self.card.update_matrix(barrel)
        print('-'*46 + '\nИгрок ' + self.name + ' зачеркнул число\n' + '-'*46)

    def pass_move(self):
        print('-'*46 + '\nИгрок ' + self.name + ' пропустил ход\n' + '-'*46)

    def lost_move(self, barrel):
        self.lost = True
        print('-'*46 + '\nИгрок ' + self.name + ' проиграл\n' + '-'*46)

    def move(self, barrel):
        '''
        :param
            barrel: номер на бочонке
        :return:
            next - следующий ход
            menu - меню игры
            win - выигрыш
        '''
        flag_barrel = False
        for i in range(len(self.card.matrix)):
            if barrel in self.card.matrix[i]:
                flag_barrel = True
        result = 'next'
        if self.owner == 'man':
            answer = input(self.name + ', выберите действие: (| 1. Зачеркнуть | 2. Продолжить | 3. Меню игры |): ')
            if answer == '1':
                if flag_barrel:
                    self.cross_number(barrel)
                else:
                    print('Этого числа ' + str(barrel) + ' нет в Вашей карточке')
                    self.lost_move(barrel)
            if answer == '2':
                if flag_barrel:
                    print('Это число ' + str(barrel) + ' есть в Вашей карточке')
                    self.lost_move(barrel)
                else:
                    self.pass_move()
            if answer == '3':
                result = 'menu'
        else:
            self.cross_number(barrel) if flag_barrel else self.pass_move()
            time.sleep(0.05)
        if self.card.full:
            result = 'win'
        return result

