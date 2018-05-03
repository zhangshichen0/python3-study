#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 客户端每过来一个请求，都开启一个线程进行处理

from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(TCPServer, ThreadingMixIn):
    pass



class MyHandler(StreamRequestHandler):

    def handle(self):
        client = self.connection
        print('The client info: ', self.client_address)
        self.wfile.write(bytes('Think you for connecting', 'utf-8')) #必须制定编码


server = Server(('127.0.0.1', 1343), MyHandler)
server.serve_forever()
