from datetime import datetime as dt
from time import time


def data_logger(data):
    try:
        with open('hw/lesson8/employee_card.csv', 'a', encoding="utf-8") as file:
            file.write(data + ', ')
            file.write('\n')
    except FileNotFoundError:
        with open('hw/lesson8/employee_card.csv', 'w', encoding="utf-8") as file:
            file.write(data + ', ')
            file.write('\n')


def print_data(data):
    print(' '.join(data))


def log_action(date):
    try:
        time = dt.now().strftime('%H:%M:%S')
        with open('hw/lesson8/log.txt', 'a', encoding="utf-8") as file:
            file.write('{} Действие: {}\n'.format(time, date))
    except FileNotFoundError:
        with open('hw/lesson8/log.txt', 'w', encoding="utf-8") as file:
            file.write('{} Действие: {}\n'.format(time, date))
