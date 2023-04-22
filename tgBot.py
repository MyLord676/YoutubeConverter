import telebot
import yaml
from youtube import convertToMP3


def main():
    try:
        with open("./Configs/Consts.yaml", "r") as yam:
            consts = yaml.safe_load(yam)
    except Exception as e:
        print("Config 'Consts.yaml' do no read", e)

    bot = telebot.TeleBot(consts['token'])

    @bot.message_handler(commands=['help'])
    def help(message):
        print("Message Received: UserId: {}, Date: {}, MessageText: {}."
              .format(message.chat.id, message.date, message.text))
        bot.send_message(message.chat.id,
                         "/mp3 {url} - для скачивания mp3")

    @bot.message_handler(commands=['mp3'])
    def mp3(message):
        print("Message Received: UserId: {}, Date: {}, MessageText: {}."
              .format(message.chat.id, message.date, message.text))
        url = message.text[5:]
        if url:
            try:
                mp3 = convertToMP3(url)
                bot.send_audio(chat_id=message.chat.id, audio=open(mp3, 'rb'))
            except Exception as e:
                print(e)
                bot.send_message(message.chat.id,
                                 "Не удалось преобразовать файл.")
        else:
            bot.send_message(message.chat.id,
                             "Введите ссылку.")

    @bot.message_handler(content_types=['text'])
    def Request(message):
        print("Message Received: UserId: {}, Date: {}, MessageText: {}."
              .format(message.chat.id, message.date, message.text))

        bot.send_message(message.chat.id,
                         "/help - для просмотра списка команд.")

    bot.infinity_polling()


if __name__ == '__main__':
    main()
