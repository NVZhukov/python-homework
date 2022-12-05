# 1'. Вычислить число Пи c заданной точностью d
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

from math import pi
import decimal

d = input('Задайте точность числа Pi: ')
decimal.getcontext().rounding = decimal.ROUND_DOWN


def number_accuracy(num: float) -> float:
    list_num = str(num).split('.')
    return round(decimal.Decimal(pi), len(list_num[1]))


print(number_accuracy(d))
