# 5'. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import sympy

f1 = open('D:/python/hw/lesson4/task5/file1.txt', 'r')
f2 = open('D:/python/hw/lesson4/task5/file2.txt', 'r')
s = f1.read() + ' + ' + f2.read()
res = sympy.simplify(s)
f3 = open('D:/python/hw/lesson4/task5/res.txt', 'w')
f3.write(str(res))
f1.close()
f2.close()
f3.close()
