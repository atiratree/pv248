import sqlite3
import sys

from data.Person import Person


class DbEngine:
    def __init__(self, conn):
        self.conn = conn

    def find_print(self, print_number):
        result = []
        cursor = self.conn.cursor()
        cursor.execute(
            "select person.name, person.born, person.died from person join score_author on person.id = score_author.composer " +
            " join score on score_author.score = score.id" +
            " join edition on edition.score = score.id" +
            " join print on print.edition = edition.id where print.id = ?",
            (print_number,))

        for row in cursor:
            result.append(Person(self.conn, row[0], row[1], row[2]))

        return result
