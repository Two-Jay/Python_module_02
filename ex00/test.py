import unittest
import random
from ft_map import ft_map

def square(x):
    return x * x

def pow(x, y):
    return x ** y

def plus_one(x : chr):
        return ord(x) + 1

class Test_ft_map(unittest.TestCase):
    test_max = 1000
    input_string = "Hello World! Hello Python Module! 0123456789"
    input_range = range(test_max)
    input_list = [random.randint(0, 1000) for i in range(test_max)]
    input_dict = {i: random.randint(0, 1000) for i in range(test_max)}

    test_not_iterable = int(42)

    def test_map_not_iterable(self):
        self.assertEqual(ft_map(square, self.test_not_iterable), None)
        # in subject, it's said that ft_map should return None if iterables is not iterable

    def test_map_string_00(self):
        self.assertEqual(list(map(plus_one, self.input_string)), list(ft_map(plus_one, self.input_string)))    
    
    def test_map_range_00(self):
        self.assertEqual(list(map(square, self.input_range)), list(ft_map(square, self.input_range)))

    def test_map_range_01(self):
        self.assertEqual(list(map(lambda x: pow(x, 3), self.input_range)), list(ft_map(lambda x: pow(x, 3), self.input_range)))

    def test_map_range_02(self):
        self.assertEqual(list(map(lambda x: pow(x, 4), self.input_range)), list(ft_map(lambda x: pow(x, 4), self.input_range)))

    def test_map_list_00(self):
        self.assertEqual(list(map(square, self.input_list)), list(ft_map(square, self.input_list)))

    def test_map_list_01(self):
        self.assertEqual(list(map(lambda x: pow(x, 3), self.input_list)), list(ft_map(lambda x: pow(x, 3), self.input_list)))

    def test_map_list_02(self):
        self.assertEqual(list(map(lambda x: pow(x, 4), self.input_list)), list(ft_map(lambda x: pow(x, 4), self.input_list)))

    def test_map_dict_00(self):
        self.assertEqual(list(map(square, self.input_dict)), list(ft_map(square, self.input_dict)))

    def test_map_dict_01(self):
        self.assertEqual(list(map(lambda x: pow(x, 3), self.input_dict)), list(ft_map(lambda x: pow(x, 3), self.input_dict)))

    def test_map_dict_02(self):
        self.assertEqual(list(map(lambda x: pow(x, 4), self.input_dict)), list(ft_map(lambda x: pow(x, 4), self.input_dict)))

       


if __name__ == '__main__':
    unittest.main()