# 3' Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

list_data = [randint(0, 10) for i in range(15)]
print(list_data)
my_list = set(list_data)
print(my_list)
