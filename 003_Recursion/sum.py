#!/usr/bin/python
# -*- coding: utf-8 -*-

def sum_r(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_r(arr[1:])

if __name__ == '__main__':
    print(sum_r([1, 2, 3, 4, 5]))
