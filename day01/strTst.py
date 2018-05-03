# 字符串操作，所有对序列的操作方法，都适用于字符串
# 注：字符串是不可变的，分片赋值是错误的
website = 'http://python.org'
#website[-3:] = 'com' # 不合法  字符串不可变
print(website)

count = website.count("h")
print(count)


# 字符串的格式化，即使用%s,表示可被代替的位置，使用%，%左边为格式化字符串，右边为值，和string中几乎一样，
# 但是当代替多个值时，需要使用元组，而不能使用list，因为list会被解释为一个值
format = 'Hello %s, %s python'
values = ('world', 'hot')
print(format % values)

# 使用模板字符串类，进行字符串格式换
import string
s = string.Template('$x, glorious $x!')
str = s.substitute(x = 'slurm')
print(str)

# 当替换字符串中部分字符时，增加${x}来明确替换结尾
s = string.Template('${x}shichen')
str = s.substitute(x = 'zhang')
print(str)

# 使用$$显示美元符号
s = string.Template('Make $$ hehe, ${x}')
str = s.substitute(x = 'slurm')
print(str)

# 使用字典替换格式化字符串
s = string.Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'; # key=thing, value=gentleman
d['action'] = 'show his socks'
str = s.substitute(d)
print(str)
print(d)

# 浮点数格式化,.后跟的是要保留的浮点数的个数
format = 'Pi with three decimals: %.3f'
from math import pi
print(format % pi)

# 简单转换
print('Price of eggs: $%d' % 42) # 整数替换
print('Hexadecimal price of eggs: %x' % 42) # 16进制

from math import pi
print('Pi: %f ....' % pi) # 3.1516923

print('Very inexact estimate of pi: %i' % pi) # 十进制整数
print('Using str: %s' % 42) # 使用str函数处理过输出
print('Using repr: %r' % 42) # 使用repr函数处理过输出

# 字符的宽度和精度（针对浮点数）%10s 宽度为10 %10.3宽度10，保留3位小数点
print('%10f' % pi) # 字段宽 10
print('%10.2f' % pi) # 字段宽10，精度2
print('')

# find 可以在较长的字符串中查找子串，有，则返回子串最左端的索引，没有则返回-1
print('12324'.find('2')) # 该方法可指定从字符串哪里到哪里查找，包含start但不包含end

# join 将序列按照指定的方式进行连接，连接的只能是字符
s = ''.join(['1','2'])
print(s)

# lower 将所有字符转换为小写
print('ASddfd'.lower())

# strip 方法去除字符串两侧的指定的字符
print('  dsddsd  '.split())




