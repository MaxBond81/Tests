import unittest
def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0  # подсчитайте общую дистанцию зайца
    for k in hare_distances:
        hare_all += k
    turtle_all = 0  # подсчитайте общую дистанцию черепахи
    for k in turtle_distances:
        turtle_all += k
    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result


class TestSomething(unittest.TestCase):

    def test_params(self):
        for i, (list_1, list_2, expected) in enumerate([
    ([5,8], [1,2], "заяц"),
    ([5,8], [10,12], "черепаха"),
    ([5,8], [5,8], "одинаково")
]):
            with self.subTest(i):
                result = solve(list_1,list_2)
                self.assertEqual(expected,result)





