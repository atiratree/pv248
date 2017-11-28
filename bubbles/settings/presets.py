from settings.settings import Settings


def get_all_presets():
    return [NEURONS, MOVING_NEURONS, HAPPY, QUICK, SMALL_RINGS, DROPS, SMALL]


NEURONS = Settings(
    max_bubble_radius=300,
    max_bubble_line_width=1,
    min_bubbles_count=2700,
    max_bubbles_count=2700,
    random_color=False,
    bubble_speed=0)
MOVING_NEURONS = Settings(
    max_bubble_radius=300,
    max_bubble_line_width=1,
    min_bubbles_count=5000,
    max_bubbles_count=5000,
    random_color=False,
    bubble_speed=10)
HAPPY = Settings(
    max_bubble_radius=200,
    max_bubble_line_width=3,
    min_bubbles_count=500,
    max_bubbles_count=500,
    bubble_speed=5)
QUICK = Settings(
    max_bubble_radius=30,
    max_bubble_line_width=2,
    min_bubbles_count=10,
    max_bubbles_count=10,
    bubble_speed=50)
SMALL_RINGS = Settings(
    max_bubble_radius=30,
    max_bubble_line_width=10,
    min_bubbles_count=300,
    max_bubbles_count=300,
    bubble_speed=10)
DROPS = Settings(
    max_bubble_radius=300,
    max_bubble_line_width=1,
    min_bubbles_count=20,
    max_bubbles_count=20,
    bubble_speed=0)
SMALL = Settings(
    max_bubble_radius=15,
    max_bubble_line_width=1,
    min_bubbles_count=300,
    max_bubbles_count=400,
    bubble_speed=0)
