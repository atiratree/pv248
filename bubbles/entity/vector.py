from util.rand import Random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x_transition(self):
        return self.x

    def get_y_transition(self):
        return self.y


class RandomVector(Vector):
    def __init__(self, settings):
        self.settings = settings
        super().__init__(Random.get_random_speed(settings.bubble_speed),
                         Random.get_random_speed(settings.bubble_speed))

    def get_x_transition(self):
        return super().get_x_transition() + (Random.get_random_speed(self.settings.bubble_speed) // 2)

    def get_y_transition(self):
        return super().get_y_transition() + (Random.get_random_speed(self.settings.bubble_speed) // 2)
