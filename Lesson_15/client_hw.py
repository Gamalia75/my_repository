import socket

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 55000))
    message = input("Input reguest to server: ")
    m = bytes(message, encoding='UTF-8')
    sock.send(m)
    data = sock.recv(1024)
    # sock.close()
    data1 = bytes.decode(data, encoding='UTF-8')
    print(f"Server answer: {data1}")
sock.close()
