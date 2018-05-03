# if elif else 控制语句
name = input("what is your name")
if name.endswith("chen"):
    print("Hello chen")
elif name.endswith("zhang"):
    print("Hello zhang")
else:
    print("not welcome")


x = "a" if True else "b"
print(x)