class Utils:
    @staticmethod
    def print(data, extra_newline=False):
        for record in data:
            print(f"{record}\n" if extra_newline else record)

    @staticmethod
    def indentation(a, b):
        return f"{a}\n\t{b}"


def readable(value, default='?'):
    return default if value is None else value
