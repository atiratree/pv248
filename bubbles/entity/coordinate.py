from random import randint


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_position(self):
        return [self.x, self.y]

    def move(self, vector):
        self.y += vector.get_y_transition()
        self.x += vector.get_x_transition()


class RandomCoordinate(Coordinate):
    def __init__(self, max_width, max_height):
        x = randint(0, max_width)
        y = randint(0, max_height)
        super().__init__(x, y)
