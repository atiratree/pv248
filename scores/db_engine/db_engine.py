import sqlite3
import sys

from data.composer import Composer
from data.person import Person
from data.print_cls import Print
from data.score import Score


class DbEngine:
    def __init__(self, conn):
        self.conn = conn

    def find_print(self, print_number):
        result = []
        cursor = self.conn.cursor()
        cursor.execute(
            "select person.id, person.name, person.born, person.died"
            " from person"
            " join score_author on person.id = score_author.composer"
            " join score on score_author.score = score.id"
            " join edition on edition.score = score.id"
            " join print on print.edition = edition.id where print.id = ?",
            (print_number,))

        for row in cursor:
            result.append(Person(self.conn, id=row[0], name=row[1], born=row[2], died=row[3]))

        return result

    def find_composers_with_scores(self, composer_name):
        composers = []
        cursor = self.conn.cursor()
        cursor.execute(
            "select person.id, person.name, person.born, person.died,"
            " print.id, print.edition, print.partiture,"
            " score.id, score.genre, score.key, score.incipit, score.year"
            " from person "
            " join score_author on person.id = score_author.composer"
            " join score on score_author.score = score.id"
            " join edition on edition.score = score.id"
            " join print on print.edition = edition.id where person.name LIKE ?",
            (f"%{composer_name}%",))

        current_person = None
        for row in cursor:
            person_id = row[0]
            if current_person is None or current_person.id != person_id:
                current_person = Composer(self.conn, id=person_id, name=row[1], born=row[2], died=row[3])
                composers.append(current_person)

            partiture = Print(self.conn, id=row[4], edition_id=row[5], partiture=row[6])
            score = Score(self.conn, id=row[7], genre=row[8], key=row[9], incipit=row[10], year=row[11], partiture_print=partiture)
            current_person.scores.append(score)
        return composers
