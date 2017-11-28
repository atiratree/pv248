from entity.circles import RandomCircles
from util.color import Color


class DrawEngine:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.circles = RandomCircles(settings, screen.get_width(), screen.get_height())

    def next_transition(self, next_state):
        self.circles.next_transition(next_state)

    def draw(self):
        self.screen.fill(Color.BLACK)
        self.circles.draw(self.screen)
