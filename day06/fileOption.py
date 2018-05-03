# 对文件进行操作

# 执行写操作
#f = open(r"/Users/shichen/program/python_project/study/day06/test.txt", mode='w')
# 覆盖文件内原有的内容
#f.write("hello")
#f.write(" world！")
#f.close()


fr = open(r"/Users/shichen/program/python_project/study/day06/test.txt", mode='r')
# 指定读取多少个字节
print(fr.read(4))
# 会接着上面继续读取
print(fr.read())
fr.close()

# 读取文件的所有数据
with open(r"/Users/shichen/program/python_project/study/day06/test.txt") as fread:
    print(fread.read()) #读取文件的所有数据

# 按行读取文件数据 readline
with open(r"/Users/shichen/program/python_project/study/day06/test.txt") as freadline:
    for i in range(3):
        print(str(i), ":", freadline.readline(), end="")
        if i == 2:
            print()
import pprint
# readlines
with open(r"/Users/shichen/program/python_project/study/day06/test.txt") as freadlines:
    pprint.pprint(freadlines.readlines())


# 懒惰行迭代，readlines是读取的所有行进内存
import fileinput

for line in fileinput.input(r"/Users/shichen/program/python_project/study/day06/test.txt"):
    print(line, end="")

print("----------")


# 文件对象是可迭代的，直接迭代文件对象，即可读取文件中的数据
for line in open(r"/Users/shichen/program/python_project/study/day06/test.txt"):
    print(line, end="")

print("----------")

import sys
# sys.stdin对象也是可迭代的
for line in sys.stdin:
    print(line)