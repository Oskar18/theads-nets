import sqlite3
from pyexpat.errors import messages

conn = sqlite3.connect("chat_server.db")
cur = conn.cursor()

# task1  vlož nového užívateľa do tabuľky users

cur.execute("""
INSERT OR IGNORE INTO users (username, password)
VALUES ('Tomáš', 'admin12345')
""")

conn.commit()


# task2
cur.execute("""SELECT * FROM users;""")
data = cur.fetchall()
print(data)

# task3
cur.execute("""SELECT username FROM users;""")
data = cur.fetchall()
for user in data:
    print(f"{user[0]}, ", end="")

print()

# task 4

"""
room_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        message TEXT NOT NULL,
"""

messages = [
    (1, 1, "m1"),
    (1, 2, "m2"),
    (2, 1, "m3"),
    (1, 3, "m4"),
    (3, 1, "m5"),
    (3, 2, "m6"),
]

cur.executemany("""
INSERT INTO messages (room_id, user_id, message)
VALUES (?, ?, ?);
""", messages)

#conn.commit()


cur.execute("""
SELECT message 
FROM messages
WHERE room_id=2;
""")
data = cur.fetchall()
print(data)


# task5
cur.execute("""
UPDATE users
SET password='NEW PASS'
WHERE username='user1'
""")

conn.commit()

cur.execute("""SELECT * FROM users;""")
data = cur.fetchall()
print(data)


# task 6
cur.execute("""
DELETE FROM messages
WHERE room_id=1
""")

conn.commit()

cur.execute("""SELECT * FROM messages;""")
data = cur.fetchall()
print(data)