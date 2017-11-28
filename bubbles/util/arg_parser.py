import argparse
from settings.settings import Settings, DefaultSettings
import settings.presets as presets


class ArgParser:
    @staticmethod
    def require_args():
        parser = argparse.ArgumentParser(usage='\n'
                                               ' - up/down ↑↓ keys to change bubble count\n'
                                               ' - press Q to quit\n'
                                               ' - press SPACE to change mode')
        parser.add_argument('-f', '--fullscreen', type=ArgParser._str2bool, nargs='?', dest='fullscreen',
                            required=False, const=True, default=DefaultSettings.full_screen, help=f'run in fullscreen')
        parser.add_argument('-m', '--mode', type=str, nargs='?', dest='mode',
                            required=False, const=True,
                            help=f'preselected modes (NEURONS, MOVING_NEURONS, HAPPY, QUICK,'
                                 f' SMALL_RINGS); removes other visual options')
        parser.add_argument('-s', '--speed', type=ArgParser._positive_int, nargs='?', dest='speed',
                            required=False, const=True, default=DefaultSettings.bubble_speed,
                            help=f'bubble speed in pixels per frame')
        parser.add_argument('-r', '--max_radius', type=ArgParser._positive_int, nargs='?', dest='max_radius',
                            required=False, const=True, default=DefaultSettings.max_bubble_radius,
                            help=f'maximum radius bubble can have before disappearing')
        parser.add_argument('-d', '--debug', type=ArgParser._str2bool, nargs='?', dest='debug',
                            required=False, const=True, default=DefaultSettings.DEBUG, help=f'debug mode; prints seed')
        parser.add_argument('-p', '--purple_color', type=ArgParser._str2bool, nargs='?', dest='purple_color',
                            required=False, const=True, default=(not DefaultSettings.random_color),
                            help=f'purple color')

        args = parser.parse_args()

        return ArgParser._as_settings(args)

    @staticmethod
    def _as_settings(args):
        mode = args.mode
        if mode:
            mode = mode.upper()

        if mode == 'NEURONS':
            settings = presets.NEURONS
        elif mode == 'MOVING_NEURONS':
            settings = presets.MOVING_NEURONS
        elif mode == 'HAPPY':
            settings = presets.HAPPY
        elif mode == 'QUICK':
            settings = presets.QUICK
        elif mode == 'SMALL_RINGS':
            settings = presets.SMALL_RINGS
        elif mode == 'DROPS':
            settings = presets.DROPS
        elif mode == 'SMALL':
            settings = presets.SMALL
        else:
            settings = Settings(
                max_bubble_radius=args.max_radius,
                random_color=(not args.purple_color),
                bubble_speed=args.speed)
        settings.full_screen = args.fullscreen
        settings.DEBUG = args.debug

        return settings

    @staticmethod
    def _str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    @staticmethod
    def _positive_int(v):
        try:
            result = int(v)
            if result < 0:
                raise argparse.ArgumentTypeError('Positive Integer value expected.')
            return result
        except Exception:
            raise argparse.ArgumentTypeError('Positive Integer value expected.')
