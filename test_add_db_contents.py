import random
import string
import sqlite3

# Initialize the database connection
db_file = 'notes_storage.db'
conn = sqlite3.connect(db_file)

# Generate 1000 random entries
for i in range(5):
    # Generate a random title consisting of 12 characters from all uppercase letters, lowercase letters,
    # and digits.
    title = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=12))
    # Generate random note content of 500 characters from all printable ascii characters (excluding whitespace).
    content = ''.join(random.choices(string.printable[:62] + string.printable[63:95] + string.printable[96:-6], k=500))
    # Insert the new note into the database
    conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()