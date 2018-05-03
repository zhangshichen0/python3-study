# 小型客户机

import socket

cs = socket.socket()

host = '127.0.0.1'
port = 1343
cs.connect((host, port))

inputdata = input("please num:")
cs.sendall(bytes(inputdata, 'utf-8'))

data = cs.recv(1024)
if data:
    # 由于接收到的是字节流，所以需要解码
    content = data.strip().decode('utf-8')
    print(content)
