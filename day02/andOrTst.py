# bool运算符 and or not
name = ''
while not name:
    name = input("what is your name\n")

if (name is not None and name.endswith("chen")):
    print("Hello")
else:
    print("error")

# 三目运算符  a if b else c 如果b为真，则返回a，否则返回c