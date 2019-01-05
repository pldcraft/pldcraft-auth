def setwise_add(tup, x):
    return tuple(sorted(set(tup) | {x}))


def setwise_remove(tup, x):
    return tuple(sorted(set(tup).difference({x})))


def setwise_union(tup1, tup2):
    return tuple(sorted(set(tup1) | set(tup2)))


def setwise_intersection(tup1, tup2):
    return tuple(sorted(set(tup1) & set(tup2)))
