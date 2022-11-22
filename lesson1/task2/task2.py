# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значение X: ')
x = bool(int(input()))
print('Введите значение Y: ')
y = bool(int(input()))
print('Введите значение Z: ')
z = bool(int(input()))

if not (x or y or z) == (not (x) and not (y) and not (z)):
    print('yes')
