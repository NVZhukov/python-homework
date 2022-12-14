from datetime import datetime as dt
from time import time


def data_logger(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('hw/lesson7/log.txt', 'a', encoding="utf-8") as file:
        file.write('{} Абонент - {}\n'.format(time, data))
    with open('hw/lesson7/log.csv', 'a', encoding="utf-8") as file:
        file.write('{} Абонент - {}\n'.format(time, data))


def print_data(data):
    print(' '.join(data))
