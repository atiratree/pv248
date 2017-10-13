import sqlite3
import os

from metadata.Block import Block
from parse.Parser import Parser

basename = 'scorelib'
txt_file = f'{basename}.txt'
db_file = f'{basename}.dat'
sql_file = f'{basename}.sql'

if __name__ == "__main__":
    if os.path.isfile(db_file):
        os.remove(db_file)

    os.system(f'sqlite3 {db_file} < {sql_file}')

    conn = sqlite3.connect(db_file)

    file = open(txt_file, 'r')

    block = Block(conn)

    for line in file:
        line = line.strip()

        if line:
            Parser.parse(line, block)
        else:
            block.store()
            block.clear()

    conn.commit()
    conn.close()
    file.close()
