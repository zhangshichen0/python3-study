# 如何使用第三方模块

import copy

# 使用dir查看模块所包含的全局方法和参数

print(dir(copy))

# 使用列表推导式，过滤掉_开头的方法和参数
print([n for n in dir(copy) if not n.startswith('_')])

# 使用__doc__查看方法或者类说明
print(copy.__doc__)

print('-' * 80)

print(copy.copy.__doc__)

# 使用__all__声明在其他模块中能够使用到的方法或者全局变量
print(copy.__all__)

# 查看源码的位置
print(copy.__file__)