from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


class SimpleLogger(Protocol):
    '''
    事件处理器，相当于netty中的netty
    '''

    def connectionMade(self):
        '''
        连接事件
        '''
        print("Got connection from ", self.transport.client)

    def connectionLost(self, reason):
        '''
        连接关闭
        :param reason:
        '''
        print(self.transport.client, " disconnected", reason)

    def dataReceived(self, data):
        '''
        接收到数据
        :param data:
        '''
        print("received data from ", self.transport.client, " data is ", data.strip().decode('utf-8'))
        self.transport.write(bytes("服务端处理了你的请求", 'UTF-8'))


factory = Factory()
factory.protocol = SimpleLogger


reactor.listenTCP(1343, factory)
reactor.run()