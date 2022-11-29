import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
message = input("Введіть 2 числа через пробіл: ")
m = bytes(message, encoding='UTF-8')
sock.send(m)
data = sock.recv(1024)
data1 = bytes.decode(data, encoding='UTF-8')
print(f"Server answer: {data1}")
sock.close()
