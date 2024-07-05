from src import VisitLogManager

if __name__ == "__main__":

    def do_all(filename):
        VisitLogObject = VisitLogManager.Log2Blacklist()
        VisitLogObject.read_apache_log(filename)
        print(VisitLogObject.check_frequencies())

    do_all("digipart-custom.log-20240407.gz")