from src import bot_identifier

if __name__ == '__main__':
    timeout = 0.2
    one = bot_identifier.BotIdentify('8.8.8.8')
    print(one.is_good_bot(timeout))
