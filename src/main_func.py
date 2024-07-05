import argparse
from VisitLogManager import Log2Blacklist
from ip_blacklist_manager import BlackListManager
from bot_identifier import IdentifyReal

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Run specific functions with parameters.')
    # parser.add_argument('function', type=str, help='The function to call')
    # parser.add_argument('params', nargs='*', help='The parameters to pass to the function')
    # args = parser.parse_args()

    def get_blacklist(filename):
        VisitLogObject = Log2Blacklist()
        VisitLogObject.read_apache_log(filename)
        return VisitLogObject.check_frequencies()

    def bot_identify(ip):
        bot_ip = IdentifyReal(ip)
        return bot_ip.is_good_bot(0.2)

    def block_ips(filename):
        ip_blocker = BlackListManager(filename)
        ip_blocker.do_all()


    def do_all(filename):
        ip_blacklist = get_blacklist(filename)
        count = 0
        for ip in ip_blacklist:
            # print(ip)
            if count % 100 == 0:
                print(count)
            is_good_bot = bot_identify(ip)
            count += 1
            # print(is_good_bot)
            if is_good_bot == False:
                with open("copy.txt", "w") as file:
                    # print(ip)
                    file.write(ip)
            else:
                # pass
                print(ip)
        # block_ips(file)



    do_all("digipart-custom.log-20240407.gz")