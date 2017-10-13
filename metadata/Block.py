from data.Edition import Edition
from data.EditionAuthor import EditionAuthor
from data.Person import Person
from data.Print import Print
from data.Score import Score
from data.ScoreAuthor import ScoreAuthor
from data.Voice import Voice


class Block:
    def __init__(self, conn):
        if not conn:
            raise Exception('needs connection to initialize')
        self.conn = conn

        self.score = Score(conn)
        self.partiture = Print(conn)
        self.edition = Edition(conn)
        self.composers = []
        self.editors = []
        self.voices = []

    def add_composer(self, name, born, died):
        self.composers.append(Person(self.conn, name, born, died))

    def add_editor(self, name, born, died):
        self.editors.append(Person(self.conn, name, born, died))

    def add_voice(self, score, name, number):
        self.voices.append(Voice(self.conn, score, number=number, name=name))

    def clear(self):
        self.score = Score(self.conn)
        self.partiture = Print(self.conn)
        self.edition = Edition(self.conn)
        self.composers.clear()
        self.editors.clear()
        self.voices.clear()

    def store(self):
        score = self.score
        conn = self.conn

        score.store()

        for composer in self.composers:
            composer.store()
            ScoreAuthor(conn, score, composer).store()

        for voice in self.voices:
            voice.score_id = score.id
            voice.store()

        self.edition.score_id = score.id
        self.edition.store()

        for editor in self.editors:
            editor.store()
            EditionAuthor(conn, self.edition, editor).store()

        self.partiture.edition_id = self.edition.id
        self.partiture.store()
