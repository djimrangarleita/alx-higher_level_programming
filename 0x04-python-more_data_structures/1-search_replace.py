#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda x: x if x != search else replace, my_list))
