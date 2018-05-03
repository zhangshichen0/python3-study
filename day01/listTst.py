# 列表，可变的序列，通过[]来表示

# in 能够检查某个成员是否在序列中

sentence = input("Sentence：")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - text_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_margin + '| ' + ' ' * text_width + '   |')
print(' ' * left_margin + '|  ' + sentence + '  |')
print(' ' * left_margin + '| ' + ' ' * text_width + '   |')
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print()

# in方法, 查看成员是否在序列中
permissions = 'rw'
flag = 'r' in permissions
print(flag)


database = [['zhang', '1234'], ['san', '2345']]
userName = input('user name: ')
pin = input('pin code: ')
isCanAccess = [userName, pin] in database
print(isCanAccess)


# 长度 最大值  最小值
str = input("please enter a str ")
print(len(str))
print(max(str))
print(min(str))

numbers = [100, 34, 678]
print(len(numbers))

# append 在序列末尾追加元素,改变原序列
numbers.append(123)
print(numbers)

# count() 元素在序列中出现的次数
numbers.count(123)

# extend 可以在列表的末尾一次性追加另一个序列的多个值，改变原序列的值
numbers.extend([1,2,3]) # 改变原序列值
others = numbers + [1,2,3]       # 原序列值不变，产生新的序列

# index 可以查看元素在序列中的位置，存在则返回位置，不存在则报异常
numbers.index(1)

# insert 在置顶的位置插入元素
numbers.insert(0, [1,2])
numbers[0:0] = [[1,2]] # 操作复杂，且不明显
print(numbers)

# pop 从序列中移除元素，默认最后一个，并返回该元素的值，可以指定删除的元素，是唯一一个既能修改列表又返回元素值（除了none）的列表方法
# 利用append和pop方法可以实现先进后出
# 利用inset(0,.)和pop可以实现先进先出
numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

# remove 从序列中移除第一个匹配项
numbers.remove(1)

# reverse 序列取反,改变列表但不返回值
numbers.reverse()
print(numbers)

# sort 必须对相同类型的元素进行排序,且是对原序列的修改
numbers.sort()
print(numbers)
# 排序但是还想保留原序列的方法，切片生成一个新的序列
x = numbers[:]
x.sort()
print(x)
print(numbers)

x = numbers # 表示x和numbers指向了同一个对象，改变任何一个，另一个也跟着改变

# sorted 对序列排序，并返回一个新的序列
y = sorted(numbers)
print(y)
print(numbers)

# sort和sorted中的参数, key reverse
x.sort(reverse=True)
sorted(x, reverse=True)

