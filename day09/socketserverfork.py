# 每个客户端对应一个子进程，该处介绍分叉技术

from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(TCPServer, ForkingMixIn):
    '''
    继承TCPServer,ForkingMixIn实现分叉
    '''
    pass



class MyHandle(StreamRequestHandler):

    def handle(self):
        client = self.connection
        clientaddr = self.client_address
        print('client info:', clientaddr)
        client.sendall(bytes('Think you connecting', encoding='utf-8'))


server = Server(('127.0.0.1', 1343), MyHandle)
server.serve_forever()