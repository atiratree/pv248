from data.DBItem import DBItem


class Print(DBItem):
    def __init__(self, conn, id=None, edition=None, partiture='N', edition_id=None):
        super().__init__(conn)
        self._id = id
        self.partiture = partiture
        self.edition_id = edition.id if edition else edition_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def fetch_id(self):
        self.cursor.execute("select id from print where id = ?",
                            (self._id,))
        return self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into print (id, partiture, edition) values (?, ?, ?)",
                            (self._id, self.partiture, self.edition_id))

    def store(self):
        self.fetch_id()
        if self.fetch_id() is None:
            self.do_store()
