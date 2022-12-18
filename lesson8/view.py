def choose_action():
    print(f"Выберите действие \nНайти карточку работника - 1\nДобавить новую карточку работника - 2\n\
Удалить карточку работника - 3\nРедактировать карточку работника - 4\nВывести все карточки - 5\nВыход - 6")
    valid = False
    while not valid:
        player_answer = input()
        try:
            player_answer = int(player_answer)
            if player_answer >= 1 and player_answer <= 2:
                valid = True
            elif player_answer == 3:
                valid = True
            elif player_answer == 4:
                valid = True
            elif player_answer == 5:
                valid = True
            elif player_answer == 6:
                valid = True
            else:
                print("Такой команды нет.\nНекорректный ввод.")
        except:
            print("Некорректный ввод. Введите число")
            continue
    return player_answer


def message():
    return input("Введите параметр поиска: ")


def change_param():
    print('Какое поле хотите изменить?')
    print(f"\nИмя работника - 1\nФамилия работника - 2\n\
Номер телефона работника - 3\nДолжность работника - 4\nПочта работника - 5")
    valid = False
    while not valid:
        player_answer = input()
        try:
            player_answer = int(player_answer)
            if player_answer == 1:
                valid = True
            elif player_answer == 2:
                valid = True
            elif player_answer == 3:
                valid = True
            elif player_answer == 4:
                valid = True
            elif player_answer == 5:
                valid = True
            else:
                print("Такой команды нет.\nНекорректный ввод.")
        except:
            print("Некорректный ввод. Введите число")
            continue
    return player_answer
