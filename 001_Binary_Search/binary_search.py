#!/usr/bin/python
# -*- coding: utf-8 -*-

def binary_search(a_list, item):
    low = 0
    high = len(a_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == item:
            return mid
        if a_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
