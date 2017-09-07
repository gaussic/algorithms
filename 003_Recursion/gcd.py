#!/usr/bin/python
# -*- coding: utf-8 -*-

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(1680, 640))
    print(gcd(640, 1680))
