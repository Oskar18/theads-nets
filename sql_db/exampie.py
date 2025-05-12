import sqlite3
from pyexpat.errors import messages

conn = sqlite3.connect("chat_server.db")
cur = conn.cursor()

cur.execute("""
SELECT id 
FROM users
WHERE username='user2'
""")

data = cur.fetchall()[0][0]

print(data)

cur.execute(f"""
SELECT room_id, message 
FROM messages
WHERE user_id={data}
""")

data = cur.fetchall()

print(data)