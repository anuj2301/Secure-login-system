import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

def handle_client(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024).decode()
    password = hashlib.sha256(password).hexdigest()
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    if cursor.fetchone():
        c.send("Login successfull".encode())
    else:
        c.send("Login failed".encode())
while True:
    c, addr = server.accept()
    threading.Thread(target=handle_client, args=(c,)).start()

