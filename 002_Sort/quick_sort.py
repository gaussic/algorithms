#!/usr/bin/python
# -*- coding: utf-8 -*-

def quick_sort(arr):
    if len(arr) < 2:
        return arr
        
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([4, 2, 1, 10, 5, 3, 100]))
    print(quick_sort([64, 25, 12, 22, 11]))
    print(quick_sort([3, 7, 4, 9, 5, 2, 6, 1]))
