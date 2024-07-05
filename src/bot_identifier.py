import socket
import concurrent.futures
import threading
import time
import multiprocessing


# socket.setdefaulttimeout(0.01)

class IdentifyReal:

    domain_list = {'Google': ['.googlebot.com', '.google', '.google.com'], 'Bing': ['.search.msn.com', '.bing.com', '.search.live.com', '.search.windows.com'], 'Yahoo': ['.yahoo.net', '.yahoo.com'], 'DuckDuckGo': ['.duckduckgo.com', '.duckduckbot.com'], 'Baidu': ['.baidu.com'], 'facebook': ['.facebook.com', 'fb.com', 'fbcdn.net'], 'twitter': ['.twitter.com', '.twimg.com', '.t.co'], 'apple': ['.apple.com'], 'amazon': ['.amazon.com']}

    def __init__(self, ip):
        self.ip = ip
        self.list_of_bots = []
    # def resolve_cname_chain(self, hostname):
    #     """
    #     Resolve the full CNAME chain for a hostname to its final destination.
    #     """
    #     try:
    #         answers = dns.resolver.resolve(hostname, 'CNAME')
    #         cname = answers[0].target.to_text().strip('.')
    #         return resolve_cname_chain(cname)
    #     except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
    #         return hostname

    def reverse_dns_lookup(self, queue):

        try:
            host_name, alias_list, ip_list = socket.gethostbyaddr(self.ip)
            print(f"IP is: {self.ip}, host_name is {host_name}")
            queue.put(host_name)
        except socket.herror:
            print("herror")
            return None
        except socket.timeout:
            print("timeout")
            return None

    def reverse_dns_with_timeout(self, timeout):
        queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=self.reverse_dns_lookup, name="Reverse_DNS_Lookup", args=(queue,))
        p.start()
        p.join(timeout)
        if p.is_alive():
            # print(f"{self.ip} timed out")
            # print("false")
            p.terminate()
            return False
        result = queue.get()
        # print(result)
        return result

    def forward_dns_lookup(self, hostname):
        try:
            # print(hostname)
            ip_addresses = socket.gethostbyname_ex(hostname)[2]
            # print(ip_addresses)
            return ip_addresses
        except socket.gaierror:
            return None

    def is_good_bot(self, timeout):
        hostname = self.reverse_dns_with_timeout(timeout)
        print(hostname)
        if hostname:
            print("hi")
            for key, value in self.domain_list.items():
                for domain in value:
                    if hostname.endswith(domain):
                        verified_ips = self.forward_dns_lookup(hostname)
                        print(verified_ips)
                        if self.ip in verified_ips:
                            self.list_of_bots.append(self.ip)
                            return True
        return False






#check for timeout,
#todo: find all the legal domain names for each good bot, search python name convention for class names/file names/varialbes/functions, then refactor, seperate test and source code diff folder, finalize all code connect with blacklist manager, final action should be given log file apply blacklisted ips to iprules blocking, functionality to create file of all the logged candidates during that run, create ticket  for linking from beginning to end