import view
import logger
import model


def employee_cads():
    while True:
        a = view.choose_action()
        if a == 1:
            find_abonent = view.message()
            res = model.search(find_abonent)
            logger.print_data(res)
            logger.log_action('Найти карточку работника')
        elif a == 2:
            res = model.add()
            logger.data_logger(res)
            logger.log_action(f'Добавить новую карточку работника {res}')
        elif a == 3:
            model.show_all()
            data = view.message()
            res = model.delete_card(data)
            logger.log_action(f'Удалить карточку работника - {data}')
        elif a == 4:
            data = view.message()
            param = view.change_param()
            model.change_card(data, param)
            res = model.search(data)
            logger.log_action(f'Изменить карточку работника - {data} {res}')
        elif a == 5:
            model.show_all()
            logger.log_action('Вывести все карточки')
        elif a == 6:
            break
