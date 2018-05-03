# 异常的处理
# raise 类似java中的 throw

class SelfDefError(Exception):
    '''
    自定义异常类
    '''
    pass

#print(help(Exception))
#print(Exception.__dict__)
#print(Exception.__bases__)


class MuffledCalculator:
    '''
    使用参数控制是否抛出异常
    '''

    muffled = False

    def calc(self, expr):
        '''
        计算表达式值
        :param expr:
        :return:
        '''
        try:
            return eval(expr)
        except (ZeroDivisionError, TypeError): # 多个异常可以使用圆括号括起来，然后异常与异常之间使用逗号隔开
            if self.muffled:
                print("Division is not allow 0")
                return 0
            else:
                raise
        finally:
            print("hahaha")

    def calc01(self, expr):
        '''
        计算表达式值
        :param expr:
        :return:
        '''
        try:
            eval(expr)
        except (ZeroDivisionError, TypeError) as e: # 使用e接收具体的异常内容，当希望捕获所有异常时，使用Exception
            print(e)
            if self.muffled:
                print("Division is not allow 0")
                return 0
            else:
                raise
        else:  # 当try中代码正常执行时，并且没有return时，走else
            print("other exception")

calculator = MuffledCalculator()
print(calculator.calc('10/2'))

print(calculator.calc01('10/10'))

calculator.muffled = True # 修改实例对应的属性值为True
print(calculator.calc('10/0'))

print(MuffledCalculator.muffled)