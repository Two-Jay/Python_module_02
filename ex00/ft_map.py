
def ft_map(function_to_apply, iterables):
    for i in iterables:
        yield function_to_apply(i)
