# 1.	Реалізувати чат без графічного інтерфейсу, який дозволить
# обмінюватися повідомленнями між клієнтом та сервером. Клієнт повинен отримувати повідомлення сервера.

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
    msg = bytes("You message was received", encoding='UTF-8')
    conn.send(msg)
conn.close()
