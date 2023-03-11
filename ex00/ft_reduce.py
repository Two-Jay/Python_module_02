from functools import reduce
from collections.abc import Iterable

def ft_reduce(function_to_apply, iterables, initial=None):
    if not hasattr(iterables, '__iter__') or not isinstance(iterables, Iterable):
        return None
    itr = iter(iterables)
    value = next(itr) if initial is None else initial
    for element in itr:
        value = function_to_apply(value, element)
    return value

if __name__ == "__main__":
    input_string = "Hello World! Hello Python Module! 0123456789"
    print(reduce(lambda x, y: x + ord(y), input_string, 0))
    print(ft_reduce(lambda x, y: x + ord(y), input_string, 0))
    
