from visit_log_manager import Log2Blacklist
from ip_blacklist_manager import BlackListManager
from bot_identifier import BotIdentify
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run specific functions with parameters.')
    parser.add_argument('function', type=str, help='The function to call')
    parser.add_argument('params', nargs='*', help='The parameters to pass to the function')
    args = parser.parse_args()

    def get_blacklist(filename):
        visit_log_manager = Log2Blacklist()
        visit_log_manager.read_apache_log(filename)
        return visit_log_manager.check_frequencies()

    def bot_identify(ip):
        bot_ip = BotIdentify(ip)
        return bot_ip.is_good_bot(0.2)

    def block_ips(filename):
        ip_blocker = BlackListManager(filename)
        ip_blocker.block_ips()

    def block_bad_bots(filename):
        ip_blacklist = get_blacklist(filename)
        bad_bot_count = 0
        for ip in ip_blacklist:
            if bad_bot_count % 100 == 0:
                print(f"Bad Bots Identified: {bad_bot_count}")
            is_good_bot = bot_identify(ip)
            if not is_good_bot:
                bad_bot_count += 1
                with open("bad_bot_file.txt", "w") as file:
                    file.write(ip)
        with open("bad_bot_file.txt", "r") as file:
            block_ips(file)


    block_bad_bots(args.params[0])
