from visit_log_manager import Log2Blacklist
from ip_blacklist_manager import BlackListManager
from bot_identifier import BotIdentify
from file_reader import whitelisted_ips, blacklisted_ips


def get_blacklist(filename, log_file_path, log_file_pattern):
    visit_log_manager = Log2Blacklist()
    visit_log_manager.read_apache_log(filename, log_file_path, log_file_pattern)
    return visit_log_manager.check_frequencies()


def bot_identify(ip, good_domain_list):
    bot_ip = BotIdentify(ip)
    bot_ip.GOOD_DOMAIN_LIST = good_domain_list
    return bot_ip.is_good_bot(0.2)


def block_ips(filename):
    ip_blocker = BlackListManager(filename)
    ip_blocker.block_ips()


def block_bad_bots(filename, log_file_path, log_file_pattern, good_domain_list):
    ip_blacklist = get_blacklist(filename, log_file_path, log_file_pattern)
    bad_bot_count = 0
    for ip in ip_blacklist:
        if bad_bot_count % 100 == 0:
            print(f"Bad Bots Identified: {bad_bot_count}")
        if ip not in whitelisted_ips:
            is_good_bot = bot_identify(ip, good_domain_list)
            if not is_good_bot or (ip in blacklisted_ips):
                bad_bot_count += 1
                with open("bad_bot_file.txt", "w") as file:
                    file.write(ip)
    with open("bad_bot_file.txt", "r") as file:
        block_ips(file)


