import unittest
import random
from loto.bag import Bag
from loto.card import Card
from loto.player import Player

class Test_Bag(unittest.TestCase):

    def setUp(self):
        self.new_bag = Bag()
        self.new_bag_2 = Bag()
        self.new_bag_3 = Bag()
        self.new_bag_3.update_barrels(90)

    def tearDown(self):
        del self.new_bag
        del self.new_bag_2

    def test_init(self):
        self.assertEqual(self.new_bag.count, 90)
        self.assertEqual(len(self.new_bag.barrels), 90)

    def test_get_barrel(self):
        count_before = self.new_bag.count
        self.assertIn(self.new_bag.get_barrel(), [i for i in range(1,91,1)])
        count_after = self.new_bag.count
        self.assertEqual(count_before - count_after, 1)

    def test_eq(self):
        self.assertTrue(self.new_bag == self.new_bag_2)

    def test_ne(self):
        self.assertFalse(self.new_bag == self.new_bag_3)

    def test_str(self):
        self.assertEqual(len(str(self.new_bag)), 446, 'длина строки не совпадает')

class Test_Card(unittest.TestCase):

    def setUp(self):
        self.new_card = Card(count_rows = 3, count_cols = 9, count_nums_in_row = 5)
        self.new_card_3 = Card(count_rows=4, count_cols=9, count_nums_in_row=5)

    def tearDown(self):
        del self.new_card

    def test_init(self):
        self.assertEqual(self.new_card.crossout, 0, 'количество зачеркнутых ячеек должно быть нулевым')
        self.assertEqual(len(self.new_card.matrix), 3, 'количество строк не совпадает')
        self.assertEqual(len(self.new_card.matrix[0]), 9, 'количество столбцов не совпадает')
        self.assertEqual(self.new_card.count_nums_in_row, 5, 'количество чисел в строке не совпадает')
        self.assertEqual(self.new_card.count_nums_in_card, 15, 'количество чисел в карте не совпадает')

    def test_update_matrix(self):
        a = 0
        for a in self.new_card.matrix[0]:
            if not a == ' ':
                break
        cross_old = self.new_card.crossout
        self.new_card.update_matrix(a)
        cross_new = self.new_card.crossout
        self.assertEqual(cross_new - cross_old, 1, 'количество зачеркнутых ячеек должно уменьшиться на 1')

    def test_eq(self):
        self.assertTrue(self.new_card == self.new_card)

    def test_ne(self):
        self.assertFalse(self.new_card == self.new_card_3)

    def test_str(self):
        self.assertEqual(len(str(self.new_card)), 140, 'длина строки не совпадает')


class Test_Player(unittest.TestCase):

    def setUp(self):
        self.new_player = Player('comp', 'comp_1')
        self.new_player_3 = Player('comp', 'comp_3')

    def tearDown(self):
        del self.new_player

    def test_int(self):
        self.assertFalse(self.new_player.lost, 'при инициализации игрок не должен быть проигравшим')
        self.assertEqual(self.new_player.name, 'comp_1', 'имя игрока не совпадает')
        self.assertEqual(self.new_player.owner, 'comp', 'тип игрока не совпадает')
        b = 0
        for b in self.new_player.card.matrix[0]:
            if not b == ' ':
                break
        if (self.new_player.owner == 'comp'):
            self.assertEqual(self.new_player.move(b), 'next', 'должен быть следующий ход')

    def test_eq(self):
        self.assertTrue(self.new_player == self.new_player)

    def test_ne(self):
        self.assertFalse(self.new_player == self.new_player_3)

    def test_str(self):
        self.assertEqual(len(str(self.new_player)), 22, 'длина строки не совпадает')



