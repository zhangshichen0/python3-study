# 实现对文件的随机访问，使用seek方法

f = open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='w')
f.write("01234567890123456789")

f.seek(5) # 移动5个字符，后开始替换
f.write("Hello World!")
f.close()

fr = open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='r')
print(fr.read())
fr.close()

# 返回当前的位置
ftell = open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='r')
print(ftell.read(3))
print(ftell.read(2))
print(ftell.tell()) # 返回当前偏移量 5
ftell.close()

# 读取行
freadline = open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='r')
print(freadline.readline())
freadline.close()

# with语句，打开文件后自动关闭
with open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='r') as f:
    print(f.readline())


# 也可使用try finally
ftry = open(r"/Users/shichen/program/python_project/study/day06/randomAccessFileT.txt", mode='r')
try:
    print(ftry.readline())
finally:
    ftry.close()
