import telebot
from random import randint

candies = 117


def candy(data):
    global candies
    candies -= data
    return candies


def can_move(move: int):
    global candies
    if move > 28:
        return False
    elif candies - move < 0:
        return False
    else:
        return True


bot = telebot.TeleBot("Тут должен быть токен")


@bot.message_handler(commands=["game"])
def start_game(message):
    bot.send_message(
        message.chat.id,
        f"Игра с конфетами\nНа столе лежит {candies} конфет\nЗа раз можно взять не больше 28",
    )


@bot.message_handler(commands=["new_game"])
def start_game(message):
    bot.send_message(
        message.chat.id, f"Мы начинаем новую игру!\nСделайте свой первый ход")
    global candies
    candies = 117


@bot.message_handler(commands=["help"])
def start_game(message):
    bot.send_message(
        message.chat.id, f"Для начала новой игры /new_game\nДля уточнения правил /game"
    )


@bot.message_handler(content_types=["text"])
def game_candy(message):
    global candies
    c = message.text
    bot_move = randint(1, 28)
    if c.isdigit():
        c = int(c)
        if can_move(c):
            bot.send_message(message.chat.id, f"Осталось {candy(c)} конфет")
            if candies < 29:
                bot.send_message(
                    message.chat.id, f"Компуктер забирает последние {candies} конфет и побежадет!")
                candies = 0
            if candies == 0:
                bot.send_message(
                    message.chat.id, "Для новой игры напишите /new_game")
        if can_move(bot_move):
            bot.send_message(
                message.chat.id,
                f"Я взял {bot_move} и осталось {candy(bot_move)} конфет",
            )
            if candies < 29:
                bot.send_message(
                    message.chat.id, f"Логично, что вы заберете последние {candies} конфет.\nПоздравляю, вы победили!")
                candies = 0
            if candies == 0:
                bot.send_message(
                    message.chat.id, "Для новой игры напишите /new_game")
    else:
        bot.send_message(
            message.chat.id,
            "Сделайте ход или, если ничего не понимаете, наберите /help",
        )


bot.infinity_polling()
