def ft_filter(function_to_apply, iterables):
    for i in iterables:
        if function_to_apply(i):
            yield i