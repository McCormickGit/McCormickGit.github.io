#imports
import sqlite3
from note_model import NoteModel


# This class handles CRUD operations for the notes table in the SQLite3 database
class NotesCRUD:
    def __init__(self, conn):
        self.conn = conn
        self.sort_method = 'title'

    # This method returns a list of NoteModel objects created from all the notes in the notes table
    def get_notes(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT id, title, content FROM notes ORDER BY {self.sort_method};")
        rows = cur.fetchall()
        notes = [NoteModel.from_tuple(row) for row in rows]
        return notes

    # This method creates a new note in the notes table with the data in the provided NoteModel
    def create_note(self, note):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO notes (title, content) VALUES (?, ?);", (note.title, note.content))
        self.conn.commit()

    # This method updates an existing note in the notes table with the data in the provided NoteModel
    def update_note(self, note):
        cur = self.conn.cursor()
        cur.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?;", (note.title, note.content, note.id))
        self.conn.commit()

    # This method deletes the note with the given note_id from the notes table
    def delete_note(self, note_id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM notes WHERE id = ?;", (note_id,))
        self.conn.commit()