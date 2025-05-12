import sqlite3



conn = sqlite3.connect("my_db.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER
)
""")

cur.execute("""
INSERT INTO users (name, age)
VALUES ('adam', 22);
""")

cur.execute("""
INSERT INTO users (name, age)
VALUES ('eva', 33);
""")

conn.commit()

cur.execute("""
SELECT *
FROM users;
""")

data = cur.fetchall()

print(data)

conn.close()