#The purpose of this code is to interface with the create_database.py
#script to use the built in python functionality of sqlite3.

#The tinker import allows for the user interface, and the time import
#allows for the use of time function to retrun runtimes.

#Planned added functionality:
#    1. Different colors for notes depending on who created it.
#    2. Selectable search algorthms to show different runtimes
#    3. Username and Password to login to the database.
#    4. Move the UI into it's own file.

#imports
import tkinter as tk
import sqlite3
import time

# Create a connection to the SQLite database file
conn = sqlite3.connect('notes.db')

# Create a Cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "notes" table if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 title TEXT NOT NULL,
                 content TEXT NOT NULL)''')

# Function to read all notes
def read_notes():
    # Clear the UI listbox
    notes_listbox.delete(0, 'end')

    # Get the current time before running the query
    start_time = time.time()

    # Get all the notes from the "notes" table
    cursor = conn.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    # Add each note to the UI listbox
    for note in notes:
        notes_listbox.insert('end', note[1])

    # Get the current time after running the query
    end_time = time.time()

    # Calculate the runtime and display it in the UI
    runtime = end_time - start_time  # Calculate the runtime in seconds
    runtime_label.config(text=f"Runtime: {runtime:.6f} seconds")  # Update the UI with the runtime

# Function to create a new note
def create_note():
    # Get the title and content of the new note from the UI
    new_title = new_title_entry.get()
    new_content = new_content_entry.get()

    # Insert the new note into the "notes" table
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (new_title, new_content))
    conn.commit()

    # Clear the UI input fields
    new_title_entry.delete(0, 'end')
    new_content_entry.delete(0, 'end')

    # Refresh the list of notes
    read_notes()

# Function to delete a note
def delete_note():
    # Get the title of the note to delete from the UI
    selected_note = notes_listbox.get('active')

    # Delete the note from the "notes" table
    cursor.execute("DELETE FROM notes WHERE title=?", (selected_note,))
    conn.commit()

    # Refresh the list of notes
    read_notes()

# Function to update a note
def update_note():
    # Get the title of the note to update from the UI
    selected_note = notes_listbox.get('active')

    # Get the updated title and content from the UI input fields
    updated_title = update_title_entry.get()
    updated_content = update_content_entry.get()

    # Update the note in the "notes" table
    cursor.execute("UPDATE notes SET title=?, content=? WHERE title=?", (updated_title, updated_content, selected_note))
    conn.commit()

    # Clear the UI input fields
    update_title_entry.delete(0, 'end')
    update_content_entry.delete(0, 'end')

    # Refresh the list of notes
    read_notes()

# Function to display the content of a note in a pop-up window
def display_note_content():
    # Get the title of the selected note from the UI
    selected_note = notes_listbox.get('active')

    # Get the content of the selected note from the "notes" table
    cursor.execute("SELECT content FROM notes WHERE title=?", (selected_note,))
    note_content = cursor.fetchone()[0]

    # Create a pop-up window to display the note content
    popup_window = tk.Toplevel(root)
    popup_window.title(f"{selected_note} Content")
    popup_label = tk.Label(popup_window, text=note_content)
    popup_label.pack()

# Initialize the Tkinter GUI framework
root = tk.Tk()

# Create a UI listbox to display the notes
notes_listbox = tk.Listbox(root)

# Add UI input fields for creating a new note
new_title_label = tk.Label(root, text='New Title:')
new_title_entry = tk.Entry(root)
new_content_label = tk.Label(root, text='New Content:')
new_content_entry = tk.Entry(root)
create_note_button = tk.Button(root, text='Create Note', command=create_note)

# Add UI elements for deleting a note
delete_note_button = tk.Button(root, text='Delete Note', command=delete_note)

# Add UI input fields for updating a note
update_title_label = tk.Label(root, text='Update Title:')
update_title_entry = tk.Entry(root)
update_content_label = tk.Label(root, text='Update Content:')
update_content_entry = tk.Entry(root)
update_note_button = tk.Button(root, text='Update Note', command=update_note)

# Add a UI element for displaying note content
display_note_button = tk.Button(root, text='Display Note', command=display_note_content)

# Add UI elements for displaying and updating the notes
read_notes_button = tk.Button(root, text='Read Notes', command=read_notes)
runtime_label = tk.Label(root, text='Runtime: 0.000000 seconds')

# Layout the UI elements
notes_listbox.grid(row=0, column=0, columnspan=3)
new_title_label.grid(row=1, column=0)
new_title_entry.grid(row=1, column=1)
new_content_label.grid(row=2, column=0)
new_content_entry.grid(row=2, column=1)
create_note_button.grid(row=3, column=1)
delete_note_button.grid(row=0, column=3)
update_title_label.grid(row=4, column=0)
update_title_entry.grid(row=4, column=1)
update_content_label.grid(row=5, column=0)
update_content_entry.grid(row=5, column=1)
update_note_button.grid(row=6, column=1)
read_notes_button.grid(row=7, column=1)
runtime_label.grid(row=8, column=1)
display_note_button.grid(row=0, column=4)

# Start the Tkinter event loop
root.mainloop()