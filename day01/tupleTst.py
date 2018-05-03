# 元组，不可变的序列，元组通过()来表示

#元组的定义
a = 1,2
print(a)

# 声明一个元素的元祖，需要在元素后加入,
a = 1,
print(a)
a = (1,)
print(a)

a = (1,2)
print(a)

# 元组的函数

# tuple 将传入的序列转换为元组,字符串也是序列
a = tuple([1,2,3]) # tuple并不是真正的方法，而是一种类型和list一样
print(a)
a = tuple('abc')
print(a)

# 分片
a = (1,2,3)
b = a[0:1]
print(b)
print(a)
# b[0] = 2 # 元组中元素不可变 ，这样报异常
# print(b)
