import unittest
def add(Nums: list[int],Target: int):
        Pushed = {}
        for i, current in enumerate(Nums):
            Expecting = Target - current
            if Expecting in Pushed:
                return [Pushed[Expecting], i]
            Pushed[current] = i
        return []
    
# Тесты
class TestAdd(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0, 1])
    def test_case_2(self):
        self.assertEqual(add([3, 2, 4], 6), [1, 2])
    def test_case_3(self):
        self.assertEqual(add([3, 3], 6), [0, 1])
    
# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)