# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)


SIZE = 3
nothing = ' . '
map = [[nothing for x in range(SIZE)]for y in range(SIZE)]


def print_map():
    print('   ', end='')
    for k in range(len(map)):
        print(str(k + 1) + '  ', end='')
    print()
    for i in range(len(map)):
        print(str(i + 1) + ' ', end='')
        for j in range(len(map[i])):
            print(map[i][j], end='')
        print()


def player_turn():
    print('Ходит первый игрок')
    x = int(input('Введите координату Х: ')) - 1
    y = int(input('Введите координату У: ')) - 1
    if (checking(x, y)):
        map[y][x] = ' X '


def player2_turn():
    print('Ходит второй игрок')
    x = int(input('Введите координату Х: ')) - 1
    y = int(input('Введите координату У: ')) - 1
    if (checking(x, y)):
        map[y][x] = ' O '


def checking(x: int, y: int):
    if (x < 0 or y < 0 or x > SIZE or y > SIZE):
        return False
    elif map[y][x] == nothing:
        return True


def check_line(chip: str):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == j and map[i][j] == chip):
                count += 1
        if count == SIZE:
            return True
        else:
            count = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == chip):
                count += 1
        if count == SIZE:
            return True
        else:
            count = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[j][i] == chip):
                count += 1
        if count == SIZE:
            return True
        else:
            count = 0

    return False


print_map()

while (True):
    player_turn()
    print_map()
    if (check_line(' X ')):
        print('Победили крестики!')
        break
    player2_turn()
    print_map()
    if (check_line(' O ')):
        print('Победили нолики!')
        break
