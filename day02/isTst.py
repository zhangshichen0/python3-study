# is is not的使用
# 二者比较的是同一性，即比较的是对象，==比较的是值
x = y = [1,2]
z = [1,2]
print(x is y)
print(z is x)
print(x == z)