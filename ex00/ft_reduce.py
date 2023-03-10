def ft_reduce(function_to_apply, iterables, initial=None):
    if not hasattr(iterables, '__iter__'):
        raise TypeError('iterables must be iterable')
    iter = iter(iterables)
    if initial is None:
        value = next(iter)
    else:
        value = initial
    for i in iter:
        value = function_to_apply(value, i)
    return value