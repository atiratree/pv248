from data.db_item import DBItem
from util.utils import readable


class Person(DBItem):
    def __init__(self, conn, id=None, name=None, born=None, died=None):
        super().__init__(conn, id)
        self.name = name
        self.born = born
        self.died = died

    def fetch_id(self):
        self.cursor.execute("select id from person where name = ?", (self.name,))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into person (name, born, died) values (?, ?, ? )",
                            (self.name, self.born, self.died))

    def do_update(self):
        self.cursor.execute("select born, died from person where name = ?", (self.name,))
        result = self.cursor.fetchone()
        if self.born is None:
            self.born = result[0]

        if self.died is None:
            self.died = result[1]

        self.cursor.execute("update person set born=?, died=? where id=?",
                            (self.born, self.died, self.id))

    def __str__(self):
        return f"{self.name} ({readable(self.born)} - {readable(self.died)})"
