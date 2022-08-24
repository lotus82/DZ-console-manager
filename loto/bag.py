import random
import collections

class Bag():
    '''
    params:
    - count - количество бочонков в мешке
    - barrels - массив чисел, соответствующий бочонкам в мешке
    '''

    def __init__(self):
        self.count = 90
        self.barrels = self.full_barrels()

    # Магические методы
    def __str__(self):
        return f'Мешок | {" | ".join(map(str, self.barrels))}'

    def __eq__(self, other):
        return collections.Counter(self.barrels) == collections.Counter(other.barrels)

    def __ne__(self, other):
        return collections.Counter(self.barrels) != collections.Counter(other.barrels)

    # -------------------
    def full_barrels(self):
        barrels = [i for i in range(1, 91, 1)]
        return barrels

    def update_barrels(self, barrel):
        if barrel in self.barrels:
            self.barrels.remove(barrel)
            self.count -= 1

    def get_barrel(self):
        num = random.choice(self.barrels)
        self.update_barrels(num)
        return num
