# 使用select实现非阻塞服务端

import socket, select


s = socket.socket()
port = 1343
s.bind(('127.0.0.1', port))
s.listen(5)

inputs = [s]

while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r == s:
            # 如果事件来自于
            c, addr = s.accept()
            print("Got connection from ", addr)
            inputs.append(c)
        else:
            try:
                r.sendall(bytes("hello", 'utf-8'))
                data = r.recv(1024)
                disconnected = not data;
            except socket.error:
                disconnected = True

            if disconnected:
                print(r.getpeername(), "disconnected")
                inputs.remove(r)
            else:
                print(data.strip().decode('utf-8'))
