# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
from random import randint

common_candy = 117
candy_first_player = 0
candy_second_player = 0
print("Жеребьевка: каждый игрок выбирает 0 или 1")
a = input('Нажмите Enter для начала')
b = int(randint(0, 1))
print(f'Первый ходит игрок загадавший {b}')


def first_player(candy: int, prize: int, move: int):
    prize += move
    candy -= move
    return candy, prize


def second_player(candy: int, prize: int, move: int):
    prize += move
    candy -= move
    return candy, prize


def who_is_win(candy: int, move: int):
    if candy - move < 0:
        print(f'Можно взять не более {candy} конфет!')
        return False
    elif move > 28:
        print('Вы пытаетесь взять слишком много конфет!')
        return False
    elif candy == 0:
        return True
    else:
        candy -= move
        return True


def print_score():
    print(f'Оставшееся количество конфет: {common_candy}')
    print(f'Конфет выиграл первый игрок: {candy_first_player}')
    print(f'Конфет выиграл второй игрок: {candy_second_player}')


while (common_candy > 0):

    if b:
        player_move = int(
            input('Ход 1 игрока.Вы можете взять от 1 до 28 конфет: '))
        first_player(common_candy, candy_first_player, player_move)
        if (who_is_win(common_candy, player_move)):
            common_candy -= player_move
            candy_first_player += player_move
        b = False

    else:
        # player_move2 = int(
        # input('Ход 2 игрока.Вы можете взять от 1 до 28 конфет: '))
        player_move2 = randint(1, 28)
        print(f'Компуктер взял {player_move2} конфет')
        second_player(common_candy, candy_second_player, player_move2)
        if (who_is_win(common_candy, player_move2)):
            common_candy -= player_move2
            candy_second_player += player_move2
        b = True
    print_score()

if candy_first_player > candy_second_player:
    print('Игра окончена!Победил первый игрок!')
    candy_first_player += candy_second_player
    print(f'Конфет выиграл первый игрок: {candy_first_player}')

elif candy_first_player < candy_second_player:
    print('Игра окончена!Победил второй игрок!')
    candy_second_player += candy_first_player
    print(f'Конфет выиграл второй игрок: {candy_second_player}')

else:
    print('Победила дружба!')
