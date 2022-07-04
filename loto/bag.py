import random

class Bag():
    '''
    params:
    - count - количество бочонков в мешке
    - barrels - массив чисел, соответствующий бочонкам в мешке
    '''

    def __init__(self):
        self.count = 90
        self.barrels = self.full_barrels()

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
