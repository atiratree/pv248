from data.DBItem import DBItem
from util.Utils import readable


class Score(DBItem):
    def __init__(self, conn, id=None, genre=None, key=None, incipit=None, year=None, partiture_print=None):
        super().__init__(conn, id)
        self.genre = genre
        self.key = key
        self.incipit = incipit
        self.year = year
        self.partiture_print = partiture_print

    def fetch_id(self):
        self.cursor.execute("select id from score where genre = ? and key = ? and year = ? and incipit = ?  ",
                            (self.genre, self.key, self.year, self.incipit))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into score (genre, key, incipit, year) values (?, ?, ?, ?)",
                            (self.genre, self.key, self.incipit, self.year))

    def __str__(self):
        return f"{self.partiture_print.id}:\t{readable(self.genre)}, " \
               f"{readable(self.key)}, {readable(self.incipit)}, {readable(self.year)}"

    @staticmethod
    def str_metadata():
        return "Print Number:\tGenre, Key, Incipit, Publication Year"
