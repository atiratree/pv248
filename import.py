import sqlite3
import os

from metadata.Block import Block
from parse.Parser import Parser
from metadata.Settings import Settings

if __name__ == "__main__":
    if os.path.isfile(Settings.db_file):
        os.remove(Settings.db_file)

    os.system(f'sqlite3 {Settings.db_file} < {Settings.sql_file}')

    with sqlite3.connect(Settings.db_file) as conn, \
            open(Settings.txt_file, 'r') as file:
        block = Block(conn)

        for line in file:
            line = line.strip()

            if line:
                Parser.parse(line, block)
            else:
                block.store()
                block.clear()

        conn.commit()
