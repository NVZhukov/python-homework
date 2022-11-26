# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('введите число: ')
n = int(input())

res = []
prod = 1
for i in range(1, n + 1):
    prod = i*prod
    res.append(prod)
print(res)
