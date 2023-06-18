# This class represents the database model for the notes table
class NoteModel:
    def __init__(self, id=None, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content

    # This class method is used to create NoteModel objects from tuples returned by queries
    @classmethod
    def from_tuple(cls, row):
        return cls(id=row[0], title=row[1], content=row[2])

    # This method is used to create string representations of NoteModel objects
    def __repr__(self):
        return f"NoteModel(id={self.id}, title='{self.title}', content='{self.content}')"