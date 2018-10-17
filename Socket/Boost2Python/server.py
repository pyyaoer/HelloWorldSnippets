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


from threading import Thread
import time

try:
    s = Thread(target=server)
    s.setDaemon(True)
    s.start()
    time.sleep(1)
except Exception as e:
    print(e)

