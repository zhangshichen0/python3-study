# 集合类型 set 不含有重复元素

# 查看可使用的方法
print([n for n in dir(set) if not n.startswith("_")])

# 创建一个集合
a = set(range(10))

b = set([1,2,3])
c = set([2,3,4])

print(b | c) # 求并集
print(b.union(c))

print(b & c) # 求交集

d=set()
d.add(frozenset(a))