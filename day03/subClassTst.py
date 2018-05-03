# 子类继承定义,当继承多个基类时，如果基类中有相同的方法，则继承基类的顺序，先继承类中的方法会覆盖后继承的类中的方法
__metaclass__=type

class Filter:

    def init(self):
        self.blocked=[]

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]



class SPAMFilter(Filter): # 继承Filter，在类名定义后，使用圆括号括起来即可，继承多个基类 用逗号隔开
    '''
    Filter子类，重写了init方法
    '''

    def init(self):
        self.blocked=['SPAM']


spamFilter = SPAMFilter();
spamFilter.init()

print(spamFilter.filter(['SPAM']))

# 判断一个类是否是另一个类的子类，使用内建函数
print(issubclass(SPAMFilter, Filter))

# 可以通过__bases__获得已知类的所有基类
print(SPAMFilter.__bases__)

# 检查实例是否是某个类的实例，这种判断方式不好
print(isinstance(spamFilter, SPAMFilter))
print(isinstance(spamFilter, Filter))

# 通过__class__或者type(o)的方式  可以获得对象属于哪个类
print(spamFilter.__class__)
print(type(spamFilter))


# 通过hasattr判断对象是否有某个方法
print(hasattr(spamFilter, "xxx"))

# 可以通过hasattr(x, "__call__"),通过getattr获得属性，通过__call__判断方法是否可调用
print(hasattr(getattr(spamFilter, "filter", None), "__call__"))

# 可以通过setattr设置属性
setattr(spamFilter, "name", "zhangshichen")
print(spamFilter.name)

# __dict__可以返回对象内所有存储的值
print(spamFilter.__dict__)
