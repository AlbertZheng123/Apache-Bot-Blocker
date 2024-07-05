from src import bot_identifier

if __name__ == '__main__':
    timeout = 2
    one = bot_identifier.IdentifyReal('8.8.8.8')
    # print(one.reverse_dns_with_timeout(0.2))
    print(one.is_good_bot(3))
