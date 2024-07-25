from apache_bot_blocker import visit_log_manager
import configparser

if __name__ == "__main__":
    def read_config():
        test_config = configparser.ConfigParser()
        test_config.read('config.ini')
        return test_config


    # In your main code or other files:
    config = read_config()
    log_file_name = 'digipart-custom.log-20240407.gz'
    log_file_location = '/home/albert/apache_log'
    log_file_format = '(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\]'
    timestamp_format = '%d/%b/%Y:%H:%M:%S %z'

    def test_visit_log_manager(filename):
        visit_log_object = visit_log_manager.Log2Blacklist()
        visit_log_object.read_apache_log(filename, log_file_location, log_file_format, timestamp_format)
        print(visit_log_object.check_frequencies(10, 60, 9, 30))

    test_visit_log_manager("digipart-custom.log-20240407.gz")