from collections.abc import Iterable

def ft_filter(function_to_apply, iterables):
    if hasattr(iterables, '__iter__') == False or isinstance(iterables, Iterable) == False:
        return None
    def core(function_to_apply, iterables):
        for i in iterables:
            if function_to_apply(i):
                yield i
    return core(function_to_apply, iterables)