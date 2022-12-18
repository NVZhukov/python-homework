def search(word):
    ab = []
    flag = True
    with open("hw/lesson8/employee_card.csv", encoding='utf-8', mode='r') as pb:
        for line_no, line in enumerate(pb):
            if word in line:
                flag = False
                ab.append(line)
        if flag:
            ab.append(f'Сотрудник {word} не найден!')
        return (ab)


def add():
    name = input('Имя: ')
    surname = input('Фамилия: ')
    phone_number = input('Номер телефона: ')
    position = input('Должность: ')
    email = input('Почта: ')
    card = [name, surname, phone_number, position, email]
    return card


def delete_card(data):
    with open("hw/lesson8/employee_card.csv", encoding='utf-8', mode='r+') as pb:
        lines = pb.readlines()
        for line in lines:
            if data in line:
                file = open("hw/lesson8/employee_card.csv",
                            encoding='utf-8', mode='r')
                f = file.read().replace(line, '')
                f2 = open("hw/lesson8/employee_card.csv",
                          encoding='utf-8', mode='w')
                f2.write(f)
                f2.close()
                file.close()


def show_all():
    with open("hw/lesson8/employee_card.csv", encoding='utf-8', mode='r+') as pb:
        lines = pb.readlines()
        print(''.join(lines))


def change_card(data, param):
    with open("hw/lesson8/employee_card.csv", encoding='utf-8', mode='r') as pb:
        lines = pb.readlines()
        for line in lines:
            if data in line:
                b = line.split(';')
                b[param - 1] = input('Введите новые данные: ')
                file = open("hw/lesson8/employee_card.csv",
                            encoding='utf-8', mode='r')
                f = file.read().replace(line, '; '.join(b))
                f2 = open("hw/lesson8/employee_card.csv",
                          encoding='utf-8', mode='w')
                f2.write(f)
                f2.close
