# 双端队列
from collections import deque

q = deque(range(5))
print(q)

q.append(5)
q.appendleft(6)

print(q)