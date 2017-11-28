from pygame import draw
from random import randint
from entity.coordinate import RandomCoordinate
from util.color import Color
from entity.vector import RandomVector


class Circle:
    def __init__(self, pos_coordinate, vector, color, radius=1, width=1, max_radius=10):
        self.color = color
        self.pos_coordinate = pos_coordinate
        self.radius = radius
        self.width = width
        self.vector = vector

        self.max_radius = max_radius

    def draw(self, screen):
        center = self.pos_coordinate.as_position()
        draw.circle(screen, self.color, center, self.radius, self.width)

    def move(self):
        self.pos_coordinate.move(self.vector)

    def expand_circle(self):
        self.radius += 1

    def is_expired(self):
        return self.radius > self.max_radius


class RandomCircle(Circle):
    def __init__(self, settings, max_width, max_height, max_nth_initial_radius=3):
        pos_coordinate = RandomCoordinate(max_width, max_height)
        vector = RandomVector(settings)
        color = Color.random_color() if settings.random_color else Color.PURPLE

        width = randint(1, settings.max_bubble_line_width)
        max_radius = randint(1, settings.max_bubble_radius)
        max_generated_radius = max_radius // max_nth_initial_radius
        if max_generated_radius < 1:
            max_generated_radius = 1

        if settings.max_bubble_line_width < max_generated_radius:
            radius = randint(settings.max_bubble_line_width, max_generated_radius)
        else:
            radius = settings.max_bubble_line_width

        super().__init__(pos_coordinate, vector, color, radius, width, max_radius)
