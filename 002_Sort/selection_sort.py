#!/usr/bin/python
# -*- coding: utf-8 -*-

def selection_sort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if i != minIndex:
            tmp = arr[i]
            arr[i] = arr[minIndex]
            arr[minIndex] = tmp
    return arr

print(selection_sort([4, 2, 1, 10, 5, 3, 100]))
print(selection_sort([64, 25, 12, 22, 11]))
