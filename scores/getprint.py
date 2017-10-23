from db_engine.db_engine import DbEngine
from metadata.Settings import Settings
from util.Utils import Utils
from parse.ArgParser import ArgParser
import sqlite3

if __name__ == "__main__":
    args = ArgParser.require_print_args()
    print_number = ArgParser.get_print_arg(args)

    with sqlite3.connect(Settings.db_file) as conn:
        db_engine = DbEngine(conn)

        result = db_engine.find_print(print_number)
        Utils.print(result)
