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

    def read_apache_log(self, filename, log_file_path, log_file_format):
        line_count = 0
        directory = log_file_path
        os.chdir(directory)
        log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\]')
        with gzip.open(filename, 'rb') as apache_log:
            for line in apache_log:
                line = line.decode('utf-8')
                pattern_match = log_pattern.match(line)
                if pattern_match:
                    line_count += 1
                    ip = pattern_match.group('ip')
                    timestamp_str = pattern_match.group('timestamp')
                    timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
                    self.ip_visit_timestamp.add_info(ip, timestamp)
                    # if line_count % 20000 == 0:
                    #     print(line_count)
                    #     if line_count == 1000000:
                    #         break
        return self.ip_visit_timestamp

    def is_frequent_visitor(self, times):
        ten_second_cond = False
        minute_cond = False
        for i in range(len(times)):
            if i + 9 < len(times) and (times[i + 9] - times[i]) <= timedelta(seconds=10):
                ten_second_cond = True
            if i + 30 < len(times) and (times[i + 30] - times[i]) <= timedelta(minutes=1):
                minute_cond = True
            # elif i + 9 >= len(times):
            #     break
            # elif i + 9 >= len(times):
            #     break
            if ten_second_cond and minute_cond:
                return True
        return False

    def check_frequencies(self):
        count = 0
        for ip, times in self.ip_visit_timestamp.information.items():
            count += 1
            # print(times)
            # print("\n")
            # print("\n")
            if self.is_frequent_visitor(times):
                # count += 1
                self.blacklist_candidates.append(ip)
                # print(ip)
                with open("second_copy.txt", "w") as file:
                    file.write(ip)
        # print(count)
        return self.blacklist_candidates
