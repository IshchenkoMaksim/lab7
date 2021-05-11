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
    x = 0

    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    A_0 = 0    
    for i in range(len(A)):
        if A[i] == 0:
            A_0 += 1

    for i in range(len(A)):
        if A[i] == min(A):
            x = i
            break    
    s = sum(A[x+1:])

    B = ()
    n = 0
    while True:
        for i in range(len(A)):
            if math.fabs(A[i]) < math.fabs(A[n]):
                n = i
        B += (A[n],)
        A = (A[:n]) + (A[n+1:])
        n = 0
        if A == ():
            break

    print(f"Отсортированный кортеж: {B}\nКоличество нулей: {A_0}\nСумма: {s}")
