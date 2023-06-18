import sqlite3

# Create a connection to the database
conn = sqlite3.connect('notes_storage.db')

# Create a new table named 'notes' if it doesn't already exist
conn.execute('''CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             content TEXT NOT NULL);''')

# Insert a new note into the 'notes' table
note = ('My First Note', 'This is the content of my first note.')
conn.execute('INSERT INTO notes (title, content) VALUES (?, ?);', note)

# Save the changes to the database
conn.commit()

# Close the database connection
conn.close()