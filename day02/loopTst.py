# 循环语句 for while

# 输出1--100的数字
x = 1;
while x <= 100:
    print(x)
    x += 1

# for
words = ["this", "is", "a", "word"]
for word in words:
    print(word)

# 使用索引循环
for i in range(len(words)):
    print("i =" + str(i), "value =" + str(words[i]))

# 循环数列
numbers = [0, 1, 2, 3, 4, 5, 6 ,7]
# range 创建一个序列 包含下限，不包含上限
print(range(0, 8))

for number in numbers:
    print(number)

for number in range(0, 10):
    print(number)

# 循环字典中的元素
d = {"x":1, "y":2, "z":3}
for key in d.keys():
    print("key =" + str(key), "value=" + str(d.get(key)))

for key, value in d.items():
    print(key, value)

# zip可以将多个序列进行合并，并返回元组,对应索引位进行合并 [(1,3),(2,4)],当序列数量不相同时，则最短的取完即停
list1 = [1, 2]
list2 = [3, 4]
print(zip(list1, list2))
for seq in zip(list1, list2):
    print(seq)

for key, value in zip(list1, list2):
    print(key, value)

# 编号迭代 同时返回index和对应的值
for index, value in enumerate(list1):
    print(index, value)

# sorted和reversed 是对序列进行排序和翻转，与sort和reverse不同的是，这两个返回新的序列或迭代对象

# 跳出循环 break

# 跳出当前循环，继续下一次循环 continue

# 列表推导式--轻量级循环
list3 = [x * x for x in range(4)]
print(list3)

list3 = [x * x for x in range(4) if x % 3 == 0]
print(list3)

girls = ["alice", "bernice"]
letterGrils = {}
for girl in girls:
    letterGrils.setdefault(girl[0], []).append(girl)

print(letterGrils)
print(letterGrils["a"])