from collections.abc import Iterable

def ft_map(function_to_apply, iterables):
    if hasattr(iterables, '__iter__') == False or isinstance(iterables, Iterable) == False:
        return None
    def core(function_to_apply, iterables):
        for i in iterables:
            yield function_to_apply(i)
    return core(function_to_apply, iterables)