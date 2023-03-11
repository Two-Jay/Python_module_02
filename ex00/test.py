import unittest
import random
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

def square(x):
    return x * x

def pow(x, y):
    return x ** y

def plus_one(x : chr):
        return ord(x) + 1

def is_even(x : int):
    return x % 2 == 0

def is_odd(x : int):
    return x % 2 == 1

def is_even_chr(x : chr):
    return ord(x) % 2 == 0

def is_odd_chr(x : chr):
    return ord(x) % 2 == 1

def is_space_chr(x : chr):
    return ord(x) == 32

class basement(unittest.TestCase):
    test_max = 1000
    input_string = "Hello World! Hello Python Module! 0123456789"
    input_range = range(test_max)
    input_list = [random.randint(0, 1000) for i in range(test_max)]
    input_dict = {i: random.randint(0, 1000) for i in range(test_max)}
    test_not_iterable = int(42)

class Test_ft_map(basement):
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

       
class Test_ft_filter(basement):
    def test_filter_not_iterable(self):
        self.assertEqual(ft_filter(square, self.test_not_iterable), None)
        # in subject, it's said that ft_filter should return None if iterables is not iterable

    def test_filter_string_00(self):
        self.assertEqual(list(filter(lambda x: is_even_chr(x), self.input_string)), \
                         list(ft_filter(lambda x: is_even_chr(x), self.input_string)))
        
    def test_filter_string_01(self):
        self.assertEqual(list(filter(lambda x: is_odd_chr(x), self.input_string)), \
                         list(ft_filter(lambda x: is_odd_chr(x), self.input_string)))
        
    def test_filter_string_02(self):
        self.assertEqual(list(filter(lambda x: is_space_chr(x), self.input_string)), \
                         list(ft_filter(lambda x: is_space_chr(x), self.input_string)))
        
    def test_filter_range_00(self):
        self.assertEqual(list(filter(lambda x: is_even(x), self.input_range)), \
                         list(ft_filter(lambda x: is_even(x), self.input_range)))
        
    def test_filter_range_01(self):
        self.assertEqual(list(filter(lambda x: is_odd(x), self.input_range)), \
                         list(ft_filter(lambda x: is_odd(x), self.input_range)))
        
    def test_filter_list_00(self):
        self.assertEqual(list(filter(lambda x: is_even(x), self.input_list)), \
                         list(ft_filter(lambda x: is_even(x), self.input_list)))
        
    def test_filter_list_01(self):
        self.assertEqual(list(filter(lambda x: is_odd(x), self.input_list)), \
                         list(ft_filter(lambda x: is_odd(x), self.input_list)))
        
    def test_filter_dict_00(self):
        self.assertEqual(list(filter(lambda x: is_even(x), self.input_dict)), \
                         list(ft_filter(lambda x: is_even(x), self.input_dict)))
        
    def test_filter_dict_01(self):
        self.assertEqual(list(filter(lambda x: is_odd(x), self.input_dict)), \
                         list(ft_filter(lambda x: is_odd(x), self.input_dict)))
        
class Test_ft_reduce(basement):
    def test_reduce_not_iterable(self):
        # self.assertEqual(ft_reduce(square, self.test_not_iterable), None)
        self.assertEqual(ft_reduce(square, self.test_not_iterable, 0), None)
        # in subject, it's said that ft_reduce should return None if iterables is not iterable

    def test_reduce_string_00(self):
        self.assertEqual(reduce(lambda x, y: x + ord(y), self.input_string, 0), ft_reduce(lambda x, y: x + ord(y), self.input_string, 0))

    def test_reduce_range_00(self):
        self.assertEqual(reduce(lambda x, y: x + y, self.input_range, 0), ft_reduce(lambda x, y: x + y, self.input_range, 0))

    def test_reduce_list_00(self):
        self.assertEqual(reduce(lambda x, y: x + y, self.input_list, 0), ft_reduce(lambda x, y: x + y, self.input_list, 0))

    def test_reduce_dict_00(self):
        self.assertEqual(reduce(lambda x, y: x + y, self.input_dict, 0), ft_reduce(lambda x, y: x + y, self.input_dict, 0))

if __name__ == '__main__':
    unittest.main()