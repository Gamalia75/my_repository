# 2.	Додайте до серверу з першого завдання функцію чат-боту,
# який би відсилав клієнту задані відповіді на певні повідомлення.

import socket
import logging


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    logging.basicConfig(level=logging.INFO, filename='hw_15.log', filemode='a', format='%(name)s - %(levelname)s - %(asctime)s - %(message)s')
    logging.warning(f"'connected:', {addr}")
    print('connected:', addr)
    data = conn.recv(1024)
    logging.info(f"'Data:', {data}")
    print(data)
    c = bytes.decode(data, encoding='UTF-8')
    if c == 'Hello':
        msg = bytes("Hi! How are you!", encoding='UTF-8')
    elif c == "Fine":
        msg = bytes("That's grate!", encoding='UTF-8')
    else:
        msg = bytes("I do not understand!", encoding='UTF-8')
        logging.error('I do not understand!')
    conn.send(msg)
conn.close()
