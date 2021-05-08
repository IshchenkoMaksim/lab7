#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# №1 В-1 Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым элементом.
# Преобразованный массив вывести.

import sys

if __name__ == '__main__':

    A = tuple(map(int, input().split()))
    i = 0
    x = 0

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    x = tuple(A[i] for i in range(len(A)) if A[i] == max(A))
    k = tuple(i for i in range(len(A)) if A[i] == max(A))
    k = k[0]

    B = x + A[1:k] + (A[0],) + A[k + 1:]
    print(B)
