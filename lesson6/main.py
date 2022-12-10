# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from random import randint
print('введите число: ')
n = int(input())
prod = 1


def multi_num(num):
    global prod
    prod = num*prod
    return prod


res = list(map(multi_num, [i for i in range(1, n+1)]))
print(res)


# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

print('введите число: ')
k = int(input())

nums_order = [(1+1/i)**i for i in range(1, k + 1)]
print(f'последовательность: {nums_order}')
print(f'сумма элементов последовательности = {sum(nums_order)}')


#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

print('введите число: ')
t = int(input())
new_list = list(map(lambda x: (-3)**x, [i for i in range(0, t)]))
print(new_list)
