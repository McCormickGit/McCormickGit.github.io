import sqlite3

# Initialize the database connection
db_file = 'notes_storage.db'
conn = sqlite3.connect(db_file)

# Execute a DELETE statement to remove all records from the notes table
conn.execute("DELETE FROM notes;")

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()