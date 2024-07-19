from bot_blocker import bot_identifier

if __name__ == '__main__':
    timeout = 0.2
    bot_id_test = bot_identifier.BotIdentify('8.8.8.8')
    bot_id_test.GOOD_DOMAIN_LIST = {'Google': ['.googlebot.com', '.google', '.google.com'],
           'Bing': ['.search.msn.com', '.bing.com', '.search.live.com', '.search.windows.com'],
           'Yahoo': ['.yahoo.net', '.yahoo.com'], 'DuckDuckGo': ['.duckduckgo.com', '.duckduckbot.com'],
           'Baidu': ['.baidu.com'], 'facebook': ['.facebook.com', 'fb.com', 'fbcdn.net'],
           'twitter': ['.twitter.com', '.twimg.com', '.t.co'], 'apple': ['.apple.com'],
           'amazon': ['.amazon.com']}
    print(bot_id_test.is_good_bot(timeout))
