# 赋值语句
x, y, z = 1, 2, 3
print(x, y, z)

# 值交换 将x的原值给了y，并没有把x=y的值赋给x
x, y = y, x
print(x, y)

# y赋给x y的值有赋给了y
x = y
y = x
print(x, y)

# 元组赋值
d = {"name": "zhang", "age":23}
key, value = d.popitem()
print(key, value)

# 元组赋值，必须保证=左右两侧的参数和值数量一致，负责异常
a, b, c = 1, 2, 3
print(a, b, c)

# 链式赋值
x = y = 3

# 增量赋值 将逻辑运算符放置在=左边
x = 2
x += 1;
x *= 2
print(x)
