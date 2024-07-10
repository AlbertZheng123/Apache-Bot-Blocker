from src import visit_log_manager

if __name__ == "__main__":

    def test_visit_log_manager(filename):
        visit_log_object = visit_log_manager.Log2Blacklist()
        visit_log_object.read_apache_log(filename)
        print(visit_log_object.check_frequencies())

    test_visit_log_manager("digipart-custom.log-20240407.gz")