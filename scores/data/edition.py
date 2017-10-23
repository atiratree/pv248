from data.db_item import DBItem


class Edition(DBItem):
    def __init__(self, conn, id=None, score=None, score_id=None, name=None, year=None):
        super().__init__(conn, id)
        self.score_id = score.id if score else score_id
        self.name = name
        self.year = year

    def fetch_id(self):
        self.cursor.execute("select id from edition where score = ? and name = ? and year = ?",
                            (self.score_id, self.name, self.year))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into edition (score, name, year) values (?, ?, ?)",
                            (self.score_id, self.name, self.year))
