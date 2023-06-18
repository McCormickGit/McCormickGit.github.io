#imports
import tkinter as tk
import time
from database_crud import NotesCRUD
from note_model import NoteModel


class NotesAppGUI:
    # Set sensible default sizes for the window, text entry widgets and buttons
    ROW_HEIGHT = 25
    TEXT_WIDTH = 40
    BUTTON_WIDTH = 12

    def __init__(self, notes_crud):
        # Create a Tkinter window
        self.window = tk.Tk()
        self.window.title('Notes App')

        # Create a list of available sorting methods
        sort_methods = ['title', 'date', 'search']

        # Create a label to display the runtime of queries
        self.runtime_label = tk.Label(self.window, text='', fg='green')
        self.runtime_label.pack()

        # Create labels for the note title and content
        self.note_title_textbox = tk.Text(self.window, height=1, width=self.TEXT_WIDTH)
        self.note_title_textbox.pack(side=tk.LEFT)
        self.note_title_label = tk.Label(self.window, text='Note Title')
        self.note_title_label.pack(side=tk.LEFT)

        self.note_content_textbox = tk.Text(self.window, height=5, width=self.TEXT_WIDTH)
        self.note_content_textbox.pack(side=tk.LEFT)
        self.note_content_label = tk.Label(self.window, text='Note Content')
        self.note_content_label.pack(side=tk.LEFT)

        # Create a listbox to display the notes
        self.notes_listbox = tk.Listbox(self.window, height=10, width=self.TEXT_WIDTH)
        self.notes_listbox.pack()

        # Create a group of radio buttons for sorting the notes
        sort_method_label = tk.Label(self.window, text='Sort by')
        sort_method_label.pack()
        self.sort_method_var = tk.StringVar(value='title')
        sort_method_dropdown = tk.OptionMenu(self.window, self.sort_method_var, *sort_methods)
        sort_method_dropdown.pack()

        # Create a text box for search terms
        self.search_textbox = tk.Text(self.window, height=1, width=self.TEXT_WIDTH)
        self.search_textbox.pack()

        # Create buttons for CRUD operations
        self.create_note_button = tk.Button(self.window, text='Create note', width=self.BUTTON_WIDTH,
                                             command=self.create_note)
        self.create_note_button.pack(side=tk.LEFT)
        self.update_note_button = tk.Button(self.window, text='Update note', width=self.BUTTON_WIDTH,
                                             command=self.update_note)
        self.update_note_button.pack(side=tk.LEFT)
        self.delete_note_button = tk.Button(self.window, text='Delete note', width=self.BUTTON_WIDTH,
                                             command=self.delete_note)
        self.delete_note_button.pack(side=tk.LEFT)

        # Fetch all the notes from the database and display them in the listbox
        self.notes_crud = notes_crud
        self.refresh_listbox()

    # Helper method to refresh the displayed notes in the listbox
    def refresh_listbox(self):
        # Clear the listbox and fetch the notes from the database
        self.notes_listbox.delete(0, tk.END)
        start_time = time.perf_counter()
        notes = self.notes_crud.get_notes()
        end_time = time.perf_counter()
        self.runtime_label.configure(text=f"Query runtime: {end_time - start_time:.6f} seconds")

        # Populate the listbox with the notes
        for note in notes:
            self.notes_listbox.insert(tk.END, note.title)

    # Helper method to retrieve the selected note from the listbox
    def get_selected_note_id(self):
        selected_indices = self.notes_listbox.curselection()
        if len(selected_indices) > 0:
            # Retrieve the NoteModel object associated with the selected note
            note_title = self.notes_listbox.get(selected_indices[0])
            note = next((note for note in self.notes_crud.get_notes() if note.title == note_title), None)
            if note:
                return note.id
        return None

    # Handler method for the create_note button
    def create_note(self):
        # Create a new NoteModel object with the contents of the text boxes
        note_title = self.note_title_textbox.get('1.0', tk.END).strip()
        note_content = self.note_content_textbox.get('1.0', tk.END).strip()
        if note_title and note_content:
            note = NoteModel(title=note_title, content=note_content)
            self.notes_crud.create_note(note)
            self.refresh_listbox()

    # Handler method for the update_note button
    def update_note(self):
        # Retrieve the selected note and update its contents
        note_id = self.get_selected_note_id()
        if note_id:
            note_title = self.note_title_textbox.get('1.0', tk.END).strip()
            note_content = self.note_content_textbox.get('1.0', tk.END).strip()
            note = NoteModel(id=note_id, title=note_title, content=note_content)
            self.notes_crud.update_note(note)
            self.refresh_listbox()

    # Handler method for the delete_note button
    def delete_note(self):
        # Retrieve the selected note and delete it from the database
        note_id = self.get_selected_note_id()
        if note_id:
            self.notes_crud.delete_note(note_id)
            self.refresh_listbox()

    # Method to run the Tkinter main loop
    def run(self):
        self.window.mainloop()