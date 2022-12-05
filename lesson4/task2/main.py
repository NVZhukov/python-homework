# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [1,2,3]
#  144 -> [2,3]

d = int(input('Задайте натуральное число: '))


def simple_multi(num: int) -> list:
    k = 2
    mylist = []
    while (num != 1):
        while (num % k == 0):
            num = num//k
            mylist.append(k)
        k = k + 1
    return mylist


print(set(simple_multi(d)))
