'''Задача 18
Требуется найти в массиве A[1..N] самый близкий по величине элемент 
к заданному числу X. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих строках 
записаны N целых чисел Ai. Последняя строка содержит число X
Пример:
5
1 2 3 4 5
6
-> 5'''

print('введите число N - количество элементов в массиве')
N = int(input())
list_1 = []
from random import randint
for i in range(N):
    i = randint(0, 10)
    list_1.append(i)
print(list_1) 
print('введите число Х - некоторое число для сравнения')
X = int(input())  
dif_min = num_close = 100 
for i in list_1:
    dif = abs(i - X)
    if dif < dif_min:
        dif_min = dif
        num_close = i
print(f'первый близкий по величине элемент {num_close}')