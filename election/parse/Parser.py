import json
from metadata.Keys import Keys as K
from utils.Utils import get_random_color


class Parser:
    @staticmethod
    def import_data(file, generated_shortcut_max_length=7):
        election = json.load(file)
        used_colors = {}

        for party in election:
            if K.short_key not in party:
                party[K.short_key] = (party[K.name_key][:generated_shortcut_max_length] if party[K.name_key] else party[
                    K.num_key]).strip()

            if K.name_key not in party:
                party[K.name_key] = party[K.short_key]

            if K.color_key in party:
                used_color = party[K.color_key]
                used_colors[used_color] = used_color

        for party in election:
            if K.color_key not in party:
                while True:
                    new_color = get_random_color()
                    if new_color not in used_colors:
                        used_colors[new_color] = new_color
                        party[K.color_key] = new_color
                        break
        return election
