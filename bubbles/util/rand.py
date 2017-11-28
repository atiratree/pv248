import random
import sys


class Random:
    def __init__(self):
        self.seed = random.randrange(sys.maxsize)
        random.seed(self.seed)

    def print_seed(self):
        print("Seed:", self.seed)

    @staticmethod
    def get_random_speed(max_speed):
        return random.randint(-max_speed, max_speed)
