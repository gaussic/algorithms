#!/usr/bin/python
# -*- coding: utf-8 -*-

def binary_search(arr, item):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess <= item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 8))