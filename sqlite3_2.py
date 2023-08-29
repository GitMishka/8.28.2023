import json
import sqlite3

# Read JSON data
with open('users.json', 'r') as f:
    users = json.load(f)

# Insert data into SQLite database
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)''')

# Insert each user into the table
for user in users:
    cursor.execute('INSERT INTO users (id, username, email) VALUES (?, ?, ?)', 
                   (user['id'], user['username'], user['email']))

connection.commit()
connection.close()
