# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

list_data = [randint(0, 10) for i in range(9)]
sum = 0
for i in range(len(list_data)):
    if i % 2 != 0:
        sum = sum + list_data[i]
print(f'Список с которым работаем: {list_data}')
print(f'Сумма элементов на нечетных позициях = {sum}')
