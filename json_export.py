import json
from database_crud import NotesCRUD

def export_notes_to_json(notes_crud, output_file):
    # retrieve all the notes from the database as a list of dictionaries
    notes = notes_crud.get_notes(as_dict=True)

    # write the notes to a JSON file
    with open(output_file, 'w') as f:
        json.dump(notes, f, indent=4)

    print(f"Notes exported to file {output_file}")