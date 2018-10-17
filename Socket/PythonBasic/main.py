import socket

HOST = 'localhost'
PORT= 52275

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data: break
        print('Server received data ' + repr(data))
        conn.sendall(data)
    conn.close()

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    print('Client received data ' + repr(data))
    s.close()


from threading import Thread
import time

try:
    s = Thread(target=server)
    c = Thread(target=client)
    s.setDaemon(True)
    s.start()
    c.start()
    time.sleep(0.1)
except Exception as e:
    print(e)

