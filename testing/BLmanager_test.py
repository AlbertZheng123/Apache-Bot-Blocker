from src import ip_blacklist_manager
import argparse


if __name__ == "__main__":
    # test_is_valid_ip()
    parser = argparse.ArgumentParser(description='Run specific functions with parameters.')
    parser.add_argument('function', type=str, help='The function to call')
    parser.add_argument('params', nargs='*', help='The parameters to pass to the function')
    args = parser.parse_args()


    def block_ips(filename):
        obj1 = ip_blacklist_manager.BlackListManager(filename)
        obj1.do_all()


    if args.function == 'block_ips':
        if len(args.params) != 1:
            print("block_ips requires 1 parameter")
        else:
            block_ips(args.params[0])