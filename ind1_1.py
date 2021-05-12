#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# №1 В-1 Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым элементом.
# Преобразованный массив вывести.

import sys

if __name__ == '__main__':

    A = tuple(map(int, input().split()))
    i = 0
    n = 0

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    n = max(a for i, a in enumerate(A))
    n = A.index(n)
    if n == 0:
        print(A)
    else:
        B = (A[n],) + A[1:n] + (A[0],) + A[n + 1:]
        print(B)
