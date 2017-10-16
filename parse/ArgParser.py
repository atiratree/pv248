import argparse


class ArgParser:
    @staticmethod
    def require_print_args():
        parser = argparse.ArgumentParser(description='Find composers by print number.')
        parser.add_argument('--print', '-p', type=int, nargs=1, dest='p', required=True,
                            help=f'filter composers by print number')
        return parser.parse_args()

    @staticmethod
    def require_composer_args():
        parser = argparse.ArgumentParser(description='Find composers by name.')
        parser.add_argument('--name', '-n', type=str, nargs=1, dest='name', required=True,
                            help=f'filter composers by name')
        return parser.parse_args()

    @staticmethod
    def get_print_arg(args):
        return args.p[0]

    @staticmethod
    def get_name_arg(args):
        return args.name[0]
