#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# №2 В-13 В списке, состоящем из вещественных элементов, вычислить:
#  1) количество элементов списка, равных 0;
#  2) сумму элементов списка, расположенных после минимального элемента.
#  Упорядочить элементы списка по возрастанию модулей элементов.

import sys
import math

if __name__ == '__main__':
    A = tuple(map(float, input().split()))

    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    A_0 = 0    
    for i in A:
        if i == 0:
            A_0 += 1

    n = 0
    for i, a in enumerate(A):
        if a < A[n]:
            n = i
    s = sum(A[n+1:])

    B = ()
    n = 0
    while True:
        for i, a in enumerate(A):
            if math.fabs(a) < math.fabs(A[n]):
                n = i
        B += (A[n],)
        A = (A[:n]) + (A[n+1:])
        n = 0
        if A == ():
            break

    print(f"Отсортированный кортеж: {B}\nКоличество нулей: {A_0}\nСумма: {s}")
