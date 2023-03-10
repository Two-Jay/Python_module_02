from collections.abc import Iterable

def ft_map(function_to_apply, iterables):
    if isinstance(iterables, Iterable) == False:
        return None
    for i in iterables:
        yield function_to_apply(i)