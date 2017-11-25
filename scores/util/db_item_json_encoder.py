from json import JSONEncoder
from sqlite3 import Cursor


class DbItemJSONEncoder(JSONEncoder):
    def default(self, o):
        return None if isinstance(o, Cursor) else o.__dict__
