from data.DBItem import DBItem


class Person(DBItem):
    def __init__(self, conn, name, born, died):
        super().__init__(conn)
        self.name = name
        self.born = born
        self.died = died

    def fetch_id(self):
        self.cursor.execute("select id from person where name = ?", (self.name,))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into person (name, born, died) values (?, ?, ? )",
                            (self.name, self.born, self.died))

    def __str__(self):
        return f"{self.name} ({self.born if self.born else '?'} - {self.died  if self.died else '?'})"
