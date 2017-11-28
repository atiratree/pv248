from pygame import display, FULLSCREEN
from engine.screensaver import ScreenSaver
from util.arg_parser import ArgParser


def run(settings):
    if settings.full_screen:
        screen = display.set_mode([0, 0], FULLSCREEN)
    else:
        screen = display.set_mode([settings.default_screen_width, settings.default_screen_height])

    screen_saver = ScreenSaver(screen, settings)
    screen_saver.run()


if __name__ == "__main__":
    run(ArgParser.require_args())
