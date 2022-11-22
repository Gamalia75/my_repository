# 3.	Напишіть сервер, який би отримував у користувача фразу,
# а потім надсилав би підраховану кількість слів у відповідь.

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    b = bytes.decode(data, encoding='UTF-8')
    d = b.split(" ")
    c = len(d)
    msg = bytes(str(c), encoding='UTF-8')
    conn.send(msg)
conn.close()
