import json
from functools import reduce

from service.composers_service import ComposersService
from util.db_item_json_encoder import DbItemJSONEncoder


class View:
    @staticmethod
    def generate_json(search_query):
        composers = ComposersService.get_composers_with_scores(search_query)
        return json.dumps(composers, cls=DbItemJSONEncoder, sort_keys=True, indent=4)

    @staticmethod
    def generate_html_view(search_query):
        composers = ComposersService.get_composers_with_scores(search_query)
        composers_list = reduce(lambda x, composer: x + f'<li>{composer}</li>', composers, '')
        return f'<br/>' + \
               f'<form>Search <input type="text" name="q" value="{search_query}"></form>' \
               f'<br/>' + \
               f'<ul>{composers_list}</ul>'
