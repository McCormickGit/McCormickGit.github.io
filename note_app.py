#Jarred McCormick, mccormickwork09@gmail.com/ 18 June 2023
#This applicaiton was made to show the growth that I made over the course
#of my CS degree.

#This application allows for users to create a database on their local machine.
#Through the user interface supported by the tinker library users can interact with
#their database.

#NOTE: JSON exports are supported if the desire to interface with another type of database.



#Imports
import sqlite3
import tkinter as tk
from binary_search_tree import BinarySearchTree
from database_crud import NotesCRUD
from notes_app_gui import NotesAppGUI

# set the name of the database file
db_file = 'notes_storage.db'

# create a database connection
notes_conn = sqlite3.connect(db_file)

# create the CRUD client for notes
notes_crud = NotesCRUD(notes_conn)

# create a binary search tree to store note titles
bst = BinarySearchTree()

# fetch all notes from the database
notes = notes_crud.get_notes()

# insert the note titles into the binary search tree
for note in notes:
    bst.insert(note.title, len(notes))  # update here

# get the notes in sorted order by doing an inorder traversal of the binary search tree
sorted_notes = [note for note_title in bst.in_order_traversal(bst.root, []) for note in notes if note.title == note_title]

# create the GUI
notes_app_gui = NotesAppGUI(notes_crud)

# update the notes listbox with the sorted notes
for note in sorted_notes:
    notes_app_gui.notes_listbox.insert(tk.END, note.title)

# start the main event loop for the GUI
notes_app_gui.window.mainloop()

# close the database connection
notes_conn.close()
