from data.DBItem import DBItem


class Score(DBItem):
    def __init__(self, conn, genre=None, key=None, incipit=None, year=None):
        super().__init__(conn)
        self.genre = genre
        self.key = key
        self.incipit = incipit
        self.year = year

    def fetch_id(self):
        self.cursor.execute("select id from score where genre = ? and key = ? and year = ? and incipit = ?  ",
                            (self.genre, self.key, self.year, self.incipit))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into score (genre, key, incipit, year) values (?, ?, ?, ?)",
                            (self.genre, self.key, self.incipit, self.year))
