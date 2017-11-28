import random


class Color:
    BLACK = [0, 0, 0]
    PURPLE = [200, 100, 232]

    @staticmethod
    def _color_part():
        return random.randint(0, 255)

    @staticmethod
    def random_color():
        return [Color._color_part(),
                Color._color_part(),
                Color._color_part()]
