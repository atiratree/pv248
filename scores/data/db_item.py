class DBItem:
    def __init__(self, conn, id=None):
        self._id = id
        self.cursor = conn.cursor()

    def store(self):
        self.fetch_id()
        if self.id is None:
            self.do_store()
            self.cursor.execute("select last_insert_rowid()")
            self.id = self.cursor.fetchone()
        else:
            self.do_update()

    def do_update(self):
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value[0] if isinstance(value, tuple) else value
