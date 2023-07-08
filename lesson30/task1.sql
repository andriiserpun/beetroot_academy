import sqlite3
conn = sqlite3.connect('task1.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER);''')
conn.execute('''ALTER TABLE users
                RENAME TO new_users;''')
conn.execute('''ALTER TABLE new_users
                ADD COLUMN email TEXT;''')
conn.execute('''INSERT INTO new_users (name, age, email)
                VALUES ('John Doe', 25, 'john@example.com'),
                       ('Jane Smith', 30, 'jane@example.com');''')
conn.execute('''UPDATE new_users
                SET age = 26
                WHERE name = 'John Doe';''')

conn.execute('''DELETE FROM new_users
                WHERE name = 'Jane Smith';''')
conn.close()