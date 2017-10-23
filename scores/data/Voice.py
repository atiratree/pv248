from data.DBItem import DBItem


class Voice(DBItem):
    def __init__(self, conn, id=None, score=None, score_id=None, number=None, name=None):
        super().__init__(conn, id)
        self.score_id = score.id if score else score_id
        self.number = number
        self.name = name

    def fetch_id(self):
        self.cursor.execute("select id from voice where score = ? and number = ? and name = ?",
                            (self.score_id, self.number, self.name))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into voice (score, number, name) values (?, ?, ?)",
                            (self.score_id, self.number, self.name))
