import pygame
from pygame import time

from engine.draw_engine import DrawEngine
from util.rand import Random
from engine.data.next_state import NextState
from settings.presets import get_all_presets


class ScreenSaver:
    def __init__(self, screen, settings):
        self.rand = Random()
        self.presets = [settings] + get_all_presets()
        if settings.DEBUG:
            self.rand.print_seed()

        self.screen = screen
        self.draw_engine = DrawEngine(self.screen, settings)

    def try_to_switch_draw_engine(self, next_state):
        if next_state.mode_changed:
            self.draw_engine = DrawEngine(self.screen, self.get_settings(next_state))

    def get_settings(self, next_state):
        return self.presets[next_state.mode_index]

    def run(self):
        clock = time.Clock()
        next_state = NextState()

        while next_state.running:
            next_state = self.process_events(pygame.event.get(), next_state)

            self.try_to_switch_draw_engine(next_state)

            self.draw_engine.next_transition(next_state)
            self.draw_engine.draw()

            pygame.display.flip()
            clock.tick(self.get_settings(next_state).frame_rate)

    def process_events(self, events, old_state):
        next_state = NextState(mode_index=old_state.mode_index)

        for ev in events:
            if ev.type == pygame.QUIT:
                next_state.running = False
            elif ev.type == pygame.KEYDOWN:
                unicode = ev.unicode
                key = ev.key

                if key == 113 or unicode == 'q':
                    next_state.running = False
                elif key == 273:  # ARROW_UP
                    next_state.add_circles = self.get_settings(old_state).add_bubbles_increment
                elif key == 274:  # ARROW_DOWN
                    next_state.add_circles = -self.get_settings(old_state).add_bubbles_increment
                elif key == 32:  # SPACE
                    next_state.mode_index += 1
                    next_state.mode_index = next_state.mode_index % len(self.presets)
                    next_state.mode_changed = True

        return next_state
