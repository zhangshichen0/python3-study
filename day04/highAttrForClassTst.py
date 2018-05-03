# 更高级的类的介绍
# 包含魔法方法，属性和迭代器

# 魔法方法：即方法前面__带两个下划线的函数

class FooBar:
    # 相当于类属性变量
    members = 0

    def __init__(self):
        '''
        构造函数
        '''
        FooBar.members = 3
        self.members = 1  # 只是修改了对象引用值
        self.membersCount = 2 # 声明为对象的属性，通过类访问不到


fooBar = FooBar()
print(FooBar.members)
print(fooBar.members)
print(fooBar.membersCount)

# 继承并重写构造函数
class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Annnnn")
            self.hungry = False
        else:
            print("no thinks")

class SongBird(Bird):
    '''
    继承Bird类，并重写构造函数
    '''

    def __init__(self):
        super(SongBird, self).__init__()  # python3之后的超类构造函数引用
        self.song = "Voice"


    def sing(self):
        print(self.song)

sb = SongBird()
sb.eat()
sb.sing()


# 魔法函数的集合
# 自实现一个无穷元素的序列
def checkIndex(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:

    def __init__(self, start = 0, step = 1):
        '''

        :param start: 算术序列开始值
        :param step:  步长
        '''
        self.start = start
        self.step = step
        self.changed = {}


    def __getitem__(self, key):
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step


    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value


seq = ArithmeticSequence(1, 2)
print(seq[5])
seq[0] = 0
print(seq[0])
print(seq)
# del seq[0] 没有实现__del__方法，所以报错


# 继承子类list实现序列
class AccessCounter(list):

    def __init__(self, *args):
        super(AccessCounter, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(AccessCounter, self).__getitem__(item)


a = AccessCounter([1,2,3])
print(a[1])
print(a.counter)


# property的使用，能够生成一个实例属性
class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0


    def getSize(self):
        return self.width, self.height

    def setSize(self, size):
        self.width, self.height = size

    size = property(getSize, setSize) # 使用property 绑定方法 property(fget,fset,fdel,doc__)

r = Rectangle()
r.width = 5
r.height = 10
print(r.size)

r.size = (100, 150)
print(r.width)


# 静态方法和类方法
class Myclass:

    @staticmethod
    def staticMethod():
        '''
        使用@staticmethod声明方法为静态方法
        :return:
        '''
        print("im a static method")


    @classmethod
    def classMethod(cls):
        '''
        使用@classmethod声明为类方法
        :return:
        '''
        print("im a class method", cls)

Myclass.staticMethod()
Myclass.classMethod()


# 迭代器
# 一个实现了__iter__的对象是可迭代的，一个实现了__next__方法的对象则是迭代器
class Fibs:

    def __init__(self):
        self.a = 0
        self.b = 1


    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        print(self.a, self.b)
        return self.a


    def __iter__(self):
        return self

fibs = Fibs()

for fib in fibs:
    if fib > 5:
        print(fib)
        break


# 从迭代器获得序列
class TestIterator:

    value = 0

    def __next__(self):
        '''
        迭代用来生成数据
        :return:
        '''
        self.value += 1
        if (self.value > 10):    # 当value>10时，停止迭代
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


testTterator = TestIterator()
print(list(testTterator))# 转换为序列


# 生成器 yield 包含yield语句的函数成为生成器
list1 = [[1,2],[3,4],[5]]
def flatten(nested):
    '''
    返回生成器对象
    :param nested:
    :return:
    '''
    for sublist in nested:
        for element in sublist:
            yield element


print(list(flatten(list1))) # [1, 2, 3, 4, 5]


# 使用迭代生成器，生成序列
def flattenIter(nested):
    '''
    无论序列嵌套几层，都可使用该方法，返回生成器
    :param nested:
    :return:
    '''
    try:
        for sublist in nested:
            # 递归 sublist有可能是列表 有可能是单独的元素，当为单独元素时，走except
            for element in flattenIter(sublist):
                yield element
    except TypeError as e:
        # print(e)
        yield nested

print(list(flattenIter([1,2,3])))


# 因为字符串也是序列，单个字符的字符串也是序列，所以会出现死循环，排除字符串

def flattenIterExcludeStr(nested):

    try:
       nested + "" # 看类型是否转换错误
    except TypeError:
        try:
            for sublist in nested:
                for element in flattenIterExcludeStr(sublist):
                    yield element
        except TypeError as e1:
            print("内部：" + str(e1))
            yield nested


def flattenIterExcludeStrOther(nested):
    try:

        try:
           nested + "" # 看类型是否转换错误
        except TypeError: pass
        else:
            print("xxx1")
            raise TypeError
        for sublist in nested:
            print("xxx2")
            for element in flattenIterExcludeStrOther(sublist):
                yield element
    except TypeError:
        print("xxx3")
        yield nested

def commonFlatten(nested):
    '''
    普通方法实现生成器
    :param nested:
    :return:
    '''
    result = []
    try:
        for sublist in nested:
            for element in sublist:
                result.append(element)
    except TypeError:
        result.append(nested)


print(list(flattenIterExcludeStrOther(['a','b','c',"s1212"])))

# 生成器的方法
def repeater(value):
    while True:
        print("xxxxxx1")
        new = (yield value)
        if new is not None:
            print("xxxxxx2")
            value = new


re = repeater(42)
print(re.__next__())
print(re.send("Hello world"))
#print(re.__next__()) #打印的是Hello world

# 希望只在本模块中运行,而不是在被导入时运行
if __name__ == '__main__':
    print(list(flattenIterExcludeStrOther(['a', 'b', 'c', "s1212"])))


# 生成器递归  回溯的应用
# 八个皇后问题

