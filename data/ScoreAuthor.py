from data.DBItem import DBItem


class ScoreAuthor(DBItem):
    def __init__(self, conn, id=None, score=None, composer=None, score_id=None, composer_id=None):
        super().__init__(conn, id)
        self.score_id = score.id if score else score_id
        self.composer_id = composer.id if composer else composer_id

    def fetch_id(self):
        self.cursor.execute("select id from score_author where score = ? and composer = ?",
                            (self.score_id, self.composer_id))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into score_author (score, composer) values (?, ?)",
                            (self.score_id, self.composer_id))
