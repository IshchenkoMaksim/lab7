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

    for i in range(len(A)):
        if A[i] == max(A):
            x = A[i]
            break

    B = (x,) + A[1:i] + (A[0],) + A[i+1:]
    print(B)
