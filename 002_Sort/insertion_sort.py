#!/usr/bin/python
# -*- coding: utf-8 -*-

def insertion_sort(arr):
    for i in range(1, len(arr)):
        minIndex = i
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            tmp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = tmp
            j -= 1
    return arr


if __name__ == '__main__':
    print(insertion_sort([4, 2, 1, 10, 5, 3, 100]))
    print(insertion_sort([64, 25, 12, 22, 11]))
    print(insertion_sort([3, 7, 4, 9, 5, 2, 6, 1]))
