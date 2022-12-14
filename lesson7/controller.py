from view import choose_action
import logger
from add_abonent import add
from search_abonent import search


def phone_book():
    a = choose_action()
    if a == 1:
        find_abonent = input('Кого ищем? ')
        res = search(find_abonent)
        logger.print_data(res)
    elif a == 2:
        res = add()
        logger.data_logger(res)
