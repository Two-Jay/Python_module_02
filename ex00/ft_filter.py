def ft_filter(function_to_apply, iterables):
    if not hasattr(iterables, '__iter__'):
        raise TypeError('iterables must be iterable')
    for i in iterables:
        if function_to_apply(i):
            yield i