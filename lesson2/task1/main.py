# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print('введите вещественное число: ')
n = input()
res = [int(x) for x in str(n) if x. isdigit()]

print(sum(res))