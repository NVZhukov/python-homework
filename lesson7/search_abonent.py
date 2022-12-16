def search(word):
    ab = []
    flag = True
    with open("hw/lesson7/log.txt", encoding='utf-8', mode='r') as pb:
        for line_no, line in enumerate(pb):
            if word in line:
                flag = False
                ab.append(line)
        if flag:
            ab.append(f'Контакт {word} не найден!')
        return (ab)
