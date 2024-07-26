import pkg_resources

def read_ip_list(resource_name):
    # Get the resource path
    data = pkg_resources.resource_string(__name__, resource_name)
    return data.decode('utf-8').splitlines()

# Access files included in the package
whitelisted_ips = read_ip_list('whitelist')
blacklisted_ips = read_ip_list('blacklist')
config_file = pkg_resources.resource_filename(__name__, 'config.ini')