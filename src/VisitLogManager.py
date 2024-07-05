import re
from datetime import datetime, timedelta
import argparse
import os
import gzip


class Log2Blacklist:


    class VisitorLog:
        def __init__(self):
            self.information = {}

        def add_info(self, ip, timestamp):
            if ip in self.information:
                self.information[ip].append(timestamp)
            else:
                self.information[ip] = [timestamp]

    def __init__(self):
        self.ip_visit_timestamp = self.VisitorLog()
        self.blacklist_candidates = []

    def read_apache_log(self, filename):
        line_count = 0
        directory = "/Users/anpei"
        os.chdir(directory)
        log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\]')
        with gzip.open(filename, 'rb') as apache_log:
            for line in apache_log:
                line = line.decode('utf-8')
                match = log_pattern.match(line)
                if match:
                    line_count += 1
                    ip = match.group('ip')
                    timestamp_str = match.group('timestamp')
                    timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
                    self.ip_visit_timestamp.add_info(ip, timestamp)
                    if line_count % 20000 == 0:
                        print(line_count)
                        if line_count == 1000000:
                            break
        return self.ip_visit_timestamp

    def is_frequent_visitor(self, times):
        first_cond = False
        second_cond = False
        for i in range(len(times)):
            if i + 9 < len(times) and (times[i+9] - times[i]) <= timedelta(seconds=10):
                first_cond = True
            if i + 30 < len(times) and (times[i + 30] - times[i]) <= timedelta(minutes=1):
                second_cond = True
            # elif i + 9 >= len(times):
            #     break
            # elif i + 9 >= len(times):
            #     break
            if first_cond and second_cond:
                return True
        return False

    def check_frequencies(self):
        count = 0
        for ip, times in self.ip_visit_timestamp.information.items():
            # count += 1
            # print(times)
            # print("\n")
            # print("\n")
            if self.is_frequent_visitor(times):
                count += 1
                self.blacklist_candidates.append(ip)
        print(count)
        return self.blacklist_candidates


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Run specific functions with parameters.')
    # parser.add_argument('function', type=str, help='The function to call')
    # parser.add_argument('params', nargs='*', help='The parameters to pass to the function')
    # args = parser.parse_args()


    def do_all(filename):
        VisitLogObject = Log2Blacklist()
        VisitLogObject.read_apache_log(filename)
        print(VisitLogObject.check_frequencies())

    do_all("digipart-custom.log-20240407.gz")
    # if args.function == 'do_all':
    #     if len(args.params) != 1:
    #         print("block_ips requires 1 parameter")
    #     else:
    #         print('started')
    #         do_all(args.params[0])


#TODO: check whether read log file or check frequent visitor is taking too long, check ip address at beginning of line,