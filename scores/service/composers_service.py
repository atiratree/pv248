from db_engine.db_engine import DbEngine
from metadata.settings import Settings
import sqlite3


class ComposersService:
    @staticmethod
    def get_composers_with_scores(composer_name):
        with sqlite3.connect(Settings.db_file) as conn:
            db_engine = DbEngine(conn)
            return db_engine.find_composers_with_scores(composer_name)
