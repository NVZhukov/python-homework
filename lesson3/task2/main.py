# Напишите программу, которая найдёт произведение пар чисел списка.

list = [2, 3, 4, 5, 6]
j = len(list)-1
multy = []
if len(list) % 2 != 0:
    for i in range(len(list)//2 + 1):
        multy.append(list[i]*list[j-i])
else:
    for i in range(len(list)//2):
        multy.append(list[i]*list[j-i])
print(multy)
