import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)')
username1 , password1 = "mike123" , hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john456", hashlib.sha256("johnpassword".encode()).hexdigest()
username3, password3 = "sarah789", hashlib.sha256("sarahpassword".encode()).hexdigest()
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username1, password1))
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username2, password2))
cur.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username3, password3))

conn.commit()