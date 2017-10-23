from db_engine.db_engine import DbEngine
from metadata.settings import Settings
from util.utils import Utils
from parse.arg_parser import ArgParser
import sqlite3

if __name__ == "__main__":
    args = ArgParser.require_composer_args()
    composer_name = ArgParser.get_name_arg(args)

    with sqlite3.connect(Settings.db_file) as conn:
        db_engine = DbEngine(conn)

        result = db_engine.find_composers_with_scores(composer_name)
        Utils.print(result, extra_newline=True)
