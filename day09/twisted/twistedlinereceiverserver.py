# 协议使用Linereceiver---TODO 和selectclient.py配合 不成功

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

class SimpleLogger(LineReceiver):
    '''
    继承自LineReceiver，可在读取到一行数据时触发事件
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

    def lineReceived(self, line):
        print('接收到的客户端信息为：', line)
        self.transport.write("服务端处理了你的消息")


factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1343, factory)
reactor.run()
