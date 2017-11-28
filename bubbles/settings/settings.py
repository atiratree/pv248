class DefaultSettings:
    min_bubbles_count = 30
    max_bubbles_count = 100
    add_bubbles_increment = 100

    max_bubble_line_width = 3
    frame_rate = 60

    default_screen_width = 800
    default_screen_height = 600

    # Settable from cmd
    random_color = True
    full_screen = False
    DEBUG = False
    bubble_speed = 10
    max_bubble_radius = 100


class Settings:
    def __init__(self, max_bubble_radius=DefaultSettings.max_bubble_radius,
                 min_bubbles_count=DefaultSettings.min_bubbles_count,
                 max_bubbles_count=DefaultSettings.max_bubbles_count,
                 add_bubbles_increment=DefaultSettings.add_bubbles_increment,
                 max_bubble_line_width=DefaultSettings.max_bubble_line_width,
                 bubble_speed=DefaultSettings.bubble_speed,
                 frame_rate=DefaultSettings.frame_rate,
                 full_screen=DefaultSettings.full_screen,
                 default_screen_width=DefaultSettings.default_screen_width,
                 default_screen_height=DefaultSettings.default_screen_height,
                 DEBUG=DefaultSettings.DEBUG,
                 random_color=DefaultSettings.random_color):
        self.min_bubbles_count = min_bubbles_count
        self.max_bubbles_count = max_bubbles_count
        self.add_bubbles_increment = add_bubbles_increment
        self.max_bubble_line_width = max_bubble_line_width

        self.frame_rate = frame_rate

        self.default_screen_width = default_screen_width
        self.default_screen_height = default_screen_height

        self.random_color = random_color
        self.full_screen = full_screen
        self.DEBUG = DEBUG
        self.bubble_speed = bubble_speed
        self.max_bubble_radius = max_bubble_radius
