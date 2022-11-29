import socket
import asyncio


async def add(el1, el2):
    await asyncio.sleep(3)
    print('Виконується додавання')
    print(f"Результат: {el1 + el2} \n")


async def sub(el1=0, el2=0):
    await asyncio.sleep(2)
    print('Виконується віднімання')
    print(f"Результат:: {el1 - el2} \n")


async def mul(el1=0, el2=0):
    await asyncio.sleep(1)
    print('Виконується множення')
    print(f"Результат:: {el1 * el2} \n")


async def div(el1=0, el2=0):
    await asyncio.sleep(0)
    print('Виконується ділення')
    print(f"Результат:: {el1 / el2} \n")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(data)
    c = bytes.decode(data, encoding='UTF-8')
    d = c.split(" ")
    el1 = int(d[0])
    el2 = int(d[1])

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(add(el1, el2)), ioloop.create_task(sub(el1, el2)), ioloop.create_task(mul(el1, el2)), ioloop.create_task(div(el1, el2))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()

    msg = bytes("Ваші дані отримано сервером!", encoding='UTF-8')
    conn.send(msg)
conn.close()
