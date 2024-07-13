from src.bad_bot_blocker import *
import configparser

if __name__ == "__main__":

    def read_config():
        config_file = configparser.ConfigParser()
        config_file.read('config_file.ini')
        return config_file

    config = read_config()
    log_file_name = config['LOG']['log_file_name']
    log_file_location = config['LOG']['log_file_path']
    log_file_format = config['LOG']['log_file_format']
    good_domain_list = config['GOOD_BOT']['good_bot']
    block_bad_bots(log_file_name, log_file_location, log_file_format, good_domain_list)
