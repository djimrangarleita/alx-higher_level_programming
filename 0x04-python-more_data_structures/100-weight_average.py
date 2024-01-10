#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    nlist = sum(list(map(lambda row: row[0] * row[1], [row for row in
                                                       my_list])))
    div = sum(list(map(lambda row: row[1], [row for row in my_list])))
    return nlist / div
