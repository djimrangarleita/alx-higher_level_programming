#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a, tuple_b = unpack_tuple(tuple_a), unpack_tuple(tuple_b)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])


def unpack_tuple(tup=()):
    if len(tup) < 1:
        return (0, 0)
    if len(tup) < 2:
        return (tup[0], 0)
    return (tup[0], tup[1])
