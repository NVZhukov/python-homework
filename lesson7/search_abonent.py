def search(word):
    ab = []
    with open("hw/lesson7/log.txt", encoding='utf-8', mode='r') as pb:
        for line_no, line in enumerate(pb):
            if word in line:
                ab.append(line)
        return (ab)
