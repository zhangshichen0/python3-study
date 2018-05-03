# poll方式，
# TODO 代码有问题，获取不到客户端发送的数据

import socket, select

s = socket.socket()

host = '127.0.0.1'
port = 1343

s.bind((host, port))
s.listen(5)

fdmap = {s.fileno(): s}

p = select.poll()
p.register(s)

while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            c, addr = s.accept()
            print("Got connection from ", addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print(fdmap[fd].getpeername(), "disconnected")
                p.unregister(fd)
                del fdmap[fd]
            else:
                print(data.strip().decode('utf-8'))
                fdmap[fd].sendall(bytes("aaa", 'utf-8'))
