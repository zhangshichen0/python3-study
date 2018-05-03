# 测试模块导入,需要增加环境变量，让python能够找到对应的代码 cat /etc/profile
from day03 import functionTst
# 使用该模块能够打开浏览器，并指定跳转的url
import webbrowser

def hello():
    print("hello")


if __name__ == '__main__':

    '''
    如果在本模块运行的话，走这段代码
    '''
    hello()


print(functionTst.findNearestNumber([1,2,0,5,1,2,4,3]))


webbrowser.open("http://www.baidu.com")