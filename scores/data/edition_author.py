from data.db_item import DBItem


class EditionAuthor(DBItem):
    def __init__(self, conn, id=None, edition=None, editor=None, edition_id=None, editor_id=None):
        super().__init__(conn, id)
        self.edition_id = edition.id if edition else edition_id
        self.editor_id = editor.id if editor else editor_id

    def fetch_id(self):
        self.cursor.execute("select id from edition_author where edition = ? and editor = ?",
                            (self.edition_id, self.editor_id))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("insert into edition_author (edition, editor) values (?, ?)",
                            (self.edition_id, self.editor_id))
