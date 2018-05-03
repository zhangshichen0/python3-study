# 类定义
__metaclass__=type

class Person:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print('Hello, world! I`m %s' % self.name)

    def methon(self):
        print("hello ....")

    def __privateMethod(self):
        '''
        私有方法，即通过类实例无法访问到
        定义私有方法：在类方法前，加__两个下划线
        foo._Person__privateMethod()  不建议这样对私有方法进行访问
        :return:
        '''
        print('Im private method')

    def _halfPrivateMethod(self):
        '''
        使用_单下划线，能够声明不需要使用这个方法，但是又能够被外部进行访问的方法
        当使用from moudle import * 时，默认不导入
        :return:
        '''
        print('Im half private method...')

def function():
    print("I donot....")

# 定义对象
foo = Person()
foo.setName("zhangshichen")
foo.methon()

foo.methon = function # 可以将类外部的函数赋给类内部的方法
foo.methon()

bar = Person()
bar.setName("shichen")

foo.getName()
foo.greet()

bar.greet()
bar.getName()

function1 = bar.methon # 也可以把类中的方法赋值给一个参数
function1()

# 私有方法的访问
foo._Person__privateMethod() # 不建议这样对私有方法进行访问

# 输出类信息
help(Person)



class MemberCounter:
    '''
    类中定义全局变量，可以供所有类实例进行访问
    '''
    members = 0

    def init(self):
        MemberCounter.members += 1


# 定义第一个实例
m1 = MemberCounter()
m1.init()
print(m1.members)  # 类的成员变量即可以通过实例访问又可以通过类直接访问
print(MemberCounter.members)

# 定义第二个实例
m2 = MemberCounter()
m2.init()
print(m2.members)
print(MemberCounter.members)


# 修改实例的参数的值
#m1.members='Two'# 只修改了实例对应空间的值
MemberCounter.members=4 # 修改了所有实例对应的变量
print(m1.members)

print(m2.members)
