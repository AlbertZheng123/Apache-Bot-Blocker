import socket
import time
import multiprocessing


class BotIdentify:

    good_domain_list = {'Google': ['.googlebot.com', '.google', '.google.com'], 'Bing': ['.search.msn.com', '.bing.com', '.search.live.com', '.search.windows.com'], 'Yahoo': ['.yahoo.net', '.yahoo.com'], 'DuckDuckGo': ['.duckduckgo.com', '.duckduckbot.com'], 'Baidu': ['.baidu.com'], 'facebook': ['.facebook.com', 'fb.com', 'fbcdn.net'], 'twitter': ['.twitter.com', '.twimg.com', '.t.co'], 'apple': ['.apple.com'], 'amazon': ['.amazon.com']}

    def __init__(self, ip):
        self.ip = ip
        self.list_of_bots = []

    def reverse_dns_lookup(self, queue):
        try:
            host_name, alias_list, ip_list = socket.gethostbyaddr(self.ip)
            print(f"IP is: {self.ip}, host_name is {host_name}")
            queue.put(host_name)

        except socket.herror:
            return None
        except socket.timeout:
            return None

    def reverse_dns_with_timeout(self, timeout):
        queue = multiprocessing.Queue()
        rdl_process = multiprocessing.Process(target=self.reverse_dns_lookup, name="Reverse_DNS_Lookup", args=(queue,))
        rdl_process.start()
        rdl_process.join(timeout)
        if rdl_process.is_alive():
            rdl_process.terminate()
            return False
        rdl_result = queue.get()
        return rdl_result

    def forward_dns_lookup(self, hostname):
        try:
            ip_addresses = socket.gethostbyname_ex(hostname)[2]
            return ip_addresses
        except socket.gaierror:
            return None

    def is_good_bot(self, timeout):
        hostname = self.reverse_dns_with_timeout(timeout)
        if hostname:
            for bots, domains in self.good_domain_list.items():
                for domain in domains:
                    if hostname.endswith(domain):
                        verified_ips = self.forward_dns_lookup(hostname)
                        if self.ip in verified_ips:
                            self.list_of_bots.append(self.ip)
                            return True
        return False
