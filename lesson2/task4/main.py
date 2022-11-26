import random
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.

print('Укажите промежуток')
n = int(input())
bill = []
for i in range(-n, n + 1):
    bill.append(i)

res = 1
# Вариант с вводом позиций с клавиатуры:
# print('сколько элементов будем умножать?')
# a = int(input())
# for i in range(a):
#     print('Введите позиции: ')
#     b = int(input())
#     res = bill[b]*res
# print(f'Произведение элементов = {res}')
print(f'изначальный список: {bill}')
bill2 = random.sample(bill, len(bill))
print(f'перемешанный список: {bill2}')

# Вариант с чтением позиций из файла:
x = open('file.txt', 'r')
res = bill[int(x.readline())] * bill[int(x.readline(2))]
print(f'Произведение элементов = {res}')
