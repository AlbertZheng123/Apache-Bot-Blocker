import socket
import multiprocessing
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BotIdentify:

    GOOD_DOMAIN_LIST = {'Google': ['.googlebot.com', '.google', '.google.com'],
                        'Bing': ['.search.msn.com', '.bing.com', '.search.live.com', '.search.windows.com'],
                        'Yahoo': ['.yahoo.net', '.yahoo.com'], 'DuckDuckGo': ['.duckduckgo.com', '.duckduckbot.com'],
                        'Baidu': ['.baidu.com'], 'facebook': ['.facebook.com', 'fb.com', 'fbcdn.net'],
                        'twitter': ['.twitter.com', '.twimg.com', '.t.co'], 'apple': ['.apple.com'],
                        'amazon': ['.amazon.com']}

    def __init__(self, ip):
        self.ip = ip
        self.list_of_bots = []

    def reverse_dns_lookup(self, queue):
        """Perform a reverse DNS lookup and put the result in the queue."""
        try:
            host_name, _, _ = socket.gethostbyaddr(self.ip)
            logger.info(f"IP is: {self.ip}, host_name is {host_name}")
            queue.put(host_name)
        except (socket.herror, socket.timeout) as e:
            logger.error(f"Error in reverse DNS lookup: {e}")
            queue.put(None)

    def reverse_dns_with_timeout(self, timeout):
        """Perform a Reverse DNS Lookup with a Timeout"""
        queue = multiprocessing.Queue()
        rdl_process = multiprocessing.Process(target=self.reverse_dns_lookup, name="Reverse_DNS_Lookup", args=(queue,))
        rdl_process.start()
        rdl_process.join(timeout)
        if rdl_process.is_alive():
            rdl_process.terminate()
            logger.warning("Reverse DNS lookup timed out")
            return False
        return queue.get()

    def forward_dns_lookup(self, hostname):
        """Performs a Forward DNS Lookup"""
        try:
            return socket.gethostbyname_ex(hostname)[2]
        except socket.gaierror:
            logger.error(f"Error in forward DNS lookup: {e}")
            return None

    def is_good_bot(self, timeout):
        """Check if the IP belongs to a good bot."""
        hostname = self.reverse_dns_with_timeout(timeout)
        if hostname:
            for bot, domains in self.GOOD_DOMAIN_LIST.items():
                if any(hostname.endswith(domain) for domain in domains):
                    verified_ips = self.forward_dns_lookup(hostname)
                    if self.ip in verified_ips:
                        self.list_of_bots.append(self.ip)
                        logger.info(f"Good bot identified: {bot} - {self.ip}")
                        return True
        logger.info(f"Not a good bot: {self.ip}")
        return False
