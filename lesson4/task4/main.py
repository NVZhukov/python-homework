# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0
from random import randint

k = int(input('Введите степень: '))


def polynomial(num: int) -> str:
    res = []
    c = '*x**'
    for i in range(num):
        if (num == 1):
            c = '*x'
            res.append(str(randint(0, 100)) + c)
        else:
            res.append(str(randint(0, 100)) + c + str(num))
        num -= 1
    res.append(str(randint(0, 100)) + ' = 0')
    return (" + ".join(res))


aquesion = polynomial(k)
print(aquesion)

with open('D:/python/hw/lesson4/task4/file.txt', 'w') as f1:
    f1.write(aquesion)
