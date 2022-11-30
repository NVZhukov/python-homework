# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def negafibonacci(s: int):
    if s == 0:
        return 0
    elif s == -1:
        return 1
    else:
        return negafibonacci(s + 2) - negafibonacci(s + 1)


n = int(input())
m = n             # Если не инициализировать новую переменную и дальше в циклах использовать 'n' все ломается((
for n in range(-n, 0):
    print(negafibonacci(n), end=" ")

for m in range(m + 1):
    print(fibonacci(m), end=" ")
