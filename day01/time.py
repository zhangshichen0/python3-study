# 时间操作类型
import time
import datetime
import timeit

# 将当前时间格式化为字符串
print(time.asctime())

print(time.localtime())

print(time.time())

print([n for n in dir(datetime) if not n.startswith("_")])
