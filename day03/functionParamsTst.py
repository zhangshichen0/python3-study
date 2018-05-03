# 函数参数 形参和实参  形参是函数定义时的参数，实参是传递的参数
# 对于 字符串 元组 数字类型是不可变的，当作为参数时，它的作用域就存在于函数中
def try_to_change(name):
    name = "zhangshichen" # 相当于重新定义了一个变量


name = "shichen"
try_to_change(name)
print(name)

# 对于引用类型的操作是改变的
def changes(list1):
    list1[0] = "zhang"


list1 = ['shi', 'chen']
#changes(list1)
print(list1)

# 序列的切片操作是生成一个新的序列
changes(list1[:])
print(list1)


# 能够根据人的firstName middleName lastName，查找对应的人的全名列表
def init(data):
    '''
    初始化数据结构，字典包含first middle last作为键
    :param data: 存储数据的数据字典
    :return: none
    '''
    data['first']={}
    data['middle']={}
    data['last']={}


def lookup(data, lable, name):
    '''
    根据lable和name查找全名列表
    :param data: 数据库
    :param lable: first middle last
    :param name: 人的firstName or middleName or lastName
    :return: 对应的用户名列表
    '''
    names = data[lable].get(name)
    return names

def store(data, full_name):
    '''
    根据用户的全名 对应的进行存储
    :param data:
    :param full_name: a b c
    :return:
    '''
    names = full_name.split();
    # 当没有中间名时，用空格代替
    if len(names) == 2 : names.insert(1, "")
    lables = ('first', 'middle', 'last')
    for name, lable in zip(names, lables):
        people = lookup(data, lable, name)
        if people:
            people.append(full_name)
        else:
            data[lable][name]=[full_name]

# 调用
storage = {}
init(storage)
store(storage, "zhang shi chen")
print(lookup(storage, 'first', 'zhang'))

# 关键字参数 能够在定义函数时，提供默认值
def hello(greating='Hello', name = 'world'):
    print('%s, %s!' % (greating, name))

hello()

# 关键字参数可以和位置参数混合使用，但是位置参数必须放在关键字参数的前面
def hello_1(name, greating='Hello', punc = ','):
    print('%s %s%s!' % (greating, punc, name))


# 支持任意多个参数,收集参数---是将所有的参数收集到一个元组中
def hell0_2(*args):
    print(args)

hell0_2(1,2,3) # (1, 2, 3)

# 支持任意多个关键字参数**，字典收集
def hello_3(**kwargs):
    print(kwargs)

hello_3(name = "zhang", age = 10) # {'name': 'zhang', 'age': 10}


# 上面的名字存储 修改为支持传入多个全名
def stores(data, *full_names):
    '''
    根据用户的全名 对应的进行存储
    :param data:
    :param full_name: a b c，z s c
    :return:
    '''
    for full_name in full_names:
        names = full_name.split();
        # 当没有中间名时，用空格代替
        if len(names) == 2: names.insert(1, "")
        lables = ('first', 'middle', 'last')
        for name, lable in zip(names, lables):
            people = lookup(data, lable, name)
            if people:
                people.append(full_name)
            else:
                data[lable][name] = [full_name]

# 调用
storage = {}
init(storage)
stores(storage, "zhang shi chen", 'z s c')
print(lookup(storage, 'first', 'z'))

# 全局变量字典
print(globals())

# 当局部变量和全局变量命名相同时，直接在函数中访问全局变量就会访问不到，使用globals可以返回全局变量的字典，从而获取全局变量
globalParamter = 1;
def testglobal():
    globalParamter1 = 2
    # 在外面定义的全局变量访问不到
    print(globalParamter1)
    print(globals().get("globalParamter"))

    # 可以使用    global 声明调用的是全局变量
    global globalParamter
    globalParamter = 3  #这样把全局变量的值由1变为了3


testglobal()
print(globalParamter)


# 函数中定义函数
def mulitplier(factor):
    def mulitplyFactor(number):
        return factor * number
    return mulitplyFactor # 返回内部定义的函数

double = mulitplier(2)
print(double(5))

print(mulitplier(3)(4))


# 递归函数
# 阶乘 n * (n-1) * (n-2)……
def jiecheng_0(n):
    '''
    非递归函数的实现
    :param n:
    :return:
    '''
    result = n;
    for i in range(1,n):
        result *= i
    return result


def jiecheng_1(n):
    if n == 1:
        return 1;
    else:
        return n * jiecheng_1(n - 1)

print(jiecheng_0(10))
print(jiecheng_1(10))


# 幂
def mi_0(num, count):
    result = 1;
    for i in range(0, count):
        result *= num;
    return result

def mi(num, count):
    if count == 0:
        return 1
    else:
        return num * mi(num, count - 1)

print(mi(-2, 3))
print(mi_0(-2, 3))



# 二分查找
def binarySearch(sequence, num, lower, upper):
    if lower == upper:
        assert num == sequence[lower]
        return lower
    else:
        middle = (lower + upper) // 2
        if num > sequence[middle]:
            return binarySearch(sequence, num, middle + 1, upper)
        else:
            return binarySearch(sequence, num, lower, middle)

print(binarySearch([1,2,3,4,5], 2, 0, 5))
