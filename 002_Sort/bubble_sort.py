#!/usr/bin/python
# -*- coding: utf-8 -*-

def bubble_sort(arr):
    swapped = True
    n = len(arr)
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                tmp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = tmp
                swapped = True
        n -= 1
    return arr


if __name__ == '__main__':
    print(bubble_sort([4, 2, 1, 10, 5, 3, 100]))
    print(bubble_sort([64, 25, 12, 22, 11]))
    print(bubble_sort([3, 7, 4, 9, 5, 2, 6, 1]))
