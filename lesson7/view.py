def choose_action():
    print(f"Выберите действие \nНайти контакт - 1\nДобавить новый - 2")
    valid = False
    while not valid:
        player_answer = input(f"Введите 1 или 2: ")
        try:
            player_answer = int(player_answer)
            if player_answer >= 1 and player_answer <= 2:
                valid = True
            else:
                print("Такой команды нет.\nНекорректный ввод. Введите 1 или 2")
        except:
            print("Некорректный ввод. Введите число")
            continue
    return player_answer
