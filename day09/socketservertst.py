# socketServer是对socket的进一步封装，可使用simpleclint.py配合使用

# https://www.cnblogs.com/sean-yao/p/7836400.html

from socketserver import TCPServer, StreamRequestHandler

class MyTcpHandler(StreamRequestHandler):
    '''
    继承StreamRequestHandler，重写handler方法处理客户端请求
    '''

    def handle(self):
        caddr = self.client_address;
        print("{} wrote".format(caddr[0]))
        print("the client connection info:", caddr)
        print("ssss:", self.request.getpeername())
        # 向客户端发送信息
        self.wfile.write(bytes("Think you connection1\n", 'utf-8'));
        self.request.send(bytes("Think you connection", 'utf-8'))


server = TCPServer(('127.0.0.1', 1343), MyTcpHandler)
server.serve_forever()