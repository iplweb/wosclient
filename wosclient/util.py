from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """
    Group iterable into n sized chunks.
    See:
        http://stackoverflow.com/a/312644/758157

    See also:
        https://stackoverflow.com/questions/5850536/how-to-chunk-a-list-in-python-3
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
