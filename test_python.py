import math
list_1 = [1,0,0,1,1,1,1,0,1,0,1,1,0,0,1]

def test_filter():
    assert len(list(filter(lambda x: x == 1, list_1))) == 9
    assert (1 in list(filter(lambda x: x == 1, list_1))) and (0 not in list(filter(lambda x: x == 1, list_1))) == True

