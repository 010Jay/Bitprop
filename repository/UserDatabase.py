import sqlite3

conn = sqlite3.connect('../user.db')
cur = conn.cursor()

# cur.execute("""
#                 CREATE TABLE user (
#                 user_id integer PRIMARY KEY,
#                 first_name text,
#                 last_name text,
#                 email_address text,
#                 cellphone text
#             )""")

# cur.execute(" INSERT INTO user VALUES (null, 'Stephan', 'Salvatore', 'salvatores@gamil.com', '0653815478')")

cur.execute("SELECT * FROM user")
print(cur.fetchall())

conn.commit()
conn.close()

