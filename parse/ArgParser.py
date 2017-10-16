import argparse


class ArgParser:
    @staticmethod
    def require_print_args():
        parser = argparse.ArgumentParser(description='Show composers.')
        parser.add_argument('--print', '-p', type=int, nargs=1, dest='p', required=True,
                            help=f'filter composers by print number')

        return parser.parse_args()

    @staticmethod
    def get_print_arg(args):
        return args.p[0]
