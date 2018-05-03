# 映射 即键值对，和java中的map一样 dict

# 定义 使用{}进行定义，key和value使用:隔开，项与项之间使用,隔开,key可以使用字符串 元组  数字
d = {"name": "zhangshichen", "age": "23"}
d = dict(name = "zhangshichen", age = 23)
items = [("name", "zhangshichen"), ("age", "23")]
d = dict(items)


# 获取key对应的值
print(d["name"])


# 一个使用映射的简单例子
people = { 'Alice': {'phone': '2341', 'addr': 'Foo drive 23'}, 'Beth' : {'phone': '9102', 'addr': 'Bar street 42'}}

labels = {'phone' : 'phone number', 'addr' : 'address'}

name = input('Name: ')
request = input('Phone number(p) or address(a)?')

if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people:
    print('%s`s %s is %s.' % (name, labels[key], people[name][key]))

# 字典的格式化字符串 在%后使用()将要替换的key写在里面
phonebook = {'Beth' : '9102', 'Alice' : '2341'}
print('Alice`s phone number is %(Alice)s.' % phonebook)

# 字典方法

# clear 清除字典所有项，无返回值
phonebook.clear()
print(phonebook)

# copy 复制 浅copy
x = {'name' : 'zhangshichen', 'machines' :['foo', 'bar', 'baz']}
y = x.copy()
print(y)
x['machines'].remove('bar')
print(x)
print(y) # x = y 因为是浅copy 指向同一个对象地址

# 与之对应的是深copy 使用copy的deepcopy
from copy import deepcopy
y = deepcopy(x)

# fromkeys 使用给定的键建立新的字典，对应的值为None，两个参数，第一个为key，第二个为value
print({}.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], ['x', 'y'])) # 每个key对应着后面的值

# get获取指定key对应的值，没有则返回None，如果使用maping[key]，没有则报错
{}.get('name')

# items方法返回迭代器对象
d = {'title' : 'Python Web Site', 'url' : 'http://www.python.org', 'spam' : 0}
print(list(d.items()))

# keys 返回key的迭代器对象 和 items的用法相同
d.keys()

# pop方法，获得给定键的值，并从字典中移除
value = d.pop('title')
print(d)

# popitem 移除项并返回项，但是没有固定的顺序，随机弹出项, 返回的是(key, value)元组
dictT = d.popitem()

# setdefault 返回对应key的值，可以设置默认值
d.setdefault('name', 'N/A') # name对应的value有，则返回value，否则返回N/A，如果不设置，当没有对应的value时，则返回none

# update 方法可以利用一个字典项更新另外一个字典项，当更新的字典项的key在原字典中没有时，就会添加到字典项中
d= {'title': 'a', 'url' :"www.baidu.com"}
x = {'titile' : 'b'}
d.update(x)
print(d)
x = {'change' : 'c'}
d.update(x)
print(d)

# values
print(list(d.values()))


