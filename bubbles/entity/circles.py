from random import randint

from entity.circle import RandomCircle


class Circles:
    def __init__(self, settings, max_width, max_height, count):
        self.settings = settings
        self.max_width = max_width
        self.max_height = max_height
        self.circles = [RandomCircle(self.settings, max_width, max_height, 1) for i in range(count)]

    def _refresh_circles(self, add_circles):
        size = len(self.circles)
        self.circles = list(filter(lambda c: not c.is_expired(), self.circles))
        diff = size + add_circles - len(self.circles)
        diff += add_circles

        if add_circles < 0:
            self.circles = self.circles[:add_circles or None]

        for i in range(0, diff):
            self.circles.append(RandomCircle(self.settings, self.max_width, self.max_height))

    def next_transition(self, next_state):
        self._refresh_circles(next_state.add_circles)

        for circle in self.circles:
            circle.move()
            circle.expand_circle()

    def draw(self, screen):
        for circle in self.circles:
            circle.draw(screen)


class RandomCircles(Circles):
    def __init__(self, settings, max_width, max_height):
        count = randint(settings.min_bubbles_count, settings.max_bubbles_count)
        super().__init__(settings, max_width, max_height, count)
