import random
import collections

class Card():
    '''
    params:
    - count_rows - количество строк в карточке
    - count_cols - количество столбцов в карточке
    - count_nums_in_row - количество чисел в строке
    - count_nums_in_card - количество чисел в карточке
    - crossout - количество зачеркнутых чисел
    - matrix - карточка (матрица (3x9) клеточек)

    methods:
    - get_numbers - получение уникальных чисел, в количестве count_nums_in_card
    - get_empty - получение номеров столбцов пустых ячеек в строке
    - get_matrix - получение сформированной карточки
    '''

    def __init__(self, count_rows = 3, count_cols = 9, count_nums_in_row = 5):
        self.count_rows = count_rows
        self.count_cols = count_cols
        self.count_nums_in_row = count_nums_in_row
        self.count_nums_in_card = count_nums_in_row * count_rows
        self.crossout = 0
        self.matrix = self.get_matrix()
        self.str_card = self.to_str()
        self.full = False

    # Магические методы
    def __str__(self):
        return self.str_card

    def __eq__(self, other):
        first_set = set(map(tuple, self.matrix))
        secnd_set = set(map(tuple, other.matrix))
        return first_set == secnd_set

    def __ne__(self, other):
        first_set = set(map(tuple, self.matrix))
        secnd_set = set(map(tuple, other.matrix))
        return first_set != secnd_set

    #-------------------
    def get_numbers(self, count_num, begin_num, end_num):
        if ((end_num - begin_num) + 1) > count_num:
            card_numbers = []
            while len(card_numbers) < count_num:
                num = random.randint(begin_num, end_num)
                if num not in card_numbers:
                    card_numbers.append(num)
            return card_numbers
        else:
            raise ValueError('[ERROR]: Количество чисел меньше, чем диапазон!')

    def get_empty(self):
        empty_cells = random.sample(range(self.count_cols), self.count_cols - self.count_nums_in_row)
        return empty_cells

    def get_matrix(self):
        matrix = [[' ' for i in range(self.count_cols)] for j in range(self.count_rows)]
        numbers = self.get_numbers(self.count_nums_in_card, 1, 90)
        k = 0
        for i in range(self.count_rows):
            empty_j = self.get_empty()
            nums_of_row = sorted(numbers[i * self.count_nums_in_row:(i+1)*self.count_nums_in_row])
            k = 0
            for j in range(self.count_cols):
                if j not in empty_j:
                    matrix[i][j] = nums_of_row[k]
                    k += 1
        return matrix

    def to_str(self):
        str_matrix = ''
        for i in range(self.count_rows):
            if i > 0:
                str_matrix += '|\n'
            for j in range(self.count_cols):
                str_matrix += ('| ' + str(self.matrix[i][j]).rjust(2, ' ') + ' ')
            if i == self.count_rows - 1:
                str_matrix += '|'
        return str_matrix

    def update_matrix(self, barrel):
        for i in range(len(self.matrix)):
            if barrel in self.matrix[i]:
                ind = self.matrix[i].index(barrel)
                self.matrix[i][ind] = '--'
                self.str_card = str(self.matrix)
                break
        count_cross = 0
        for i in range(len(self.matrix)):
            count_cross += self.matrix[i].count('--')
        self.crossout += count_cross
        if count_cross == self.count_nums_in_card:
            self.full = True

