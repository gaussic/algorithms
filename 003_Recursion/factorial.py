#!/usr/bin/python
# -*- coding: utf-8 -*-

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(3))
    print(factorial(10))
