#服务机

import socket

sot = socket.socket()

host = '127.0.0.1'
port = 1343

sot.bind((host, port))

sot.listen(10)

while True:
    c, addr = sot.accept()
    print('Got client connect, addr:', addr)
    c.send(bytes('%s' % "Thank you for connecting", 'utf-8')) #python3中只接受bytes类型的数据
    c.close()