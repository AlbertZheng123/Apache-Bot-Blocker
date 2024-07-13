from src import visit_log_manager

if __name__ == "__main__":
    def read_config():
        test_config = configparser.ConfigParser()
        test_config.read('config.ini')
        return config


    # In your main code or other files:
    config = read_config()
    log_file_name = config['LOG']['log_file_name']
    log_file_location = config['LOG']['log_file_path']
    log_file_format = config['LOG']['log_file_format']


    def test_visit_log_manager(filename):
        visit_log_object = visit_log_manager.Log2Blacklist()
        visit_log_object.read_apache_log(filename, log_file_location, log_file_format)
        print(visit_log_object.check_frequencies())

    test_visit_log_manager("digipart-custom.log-20240407.gz")