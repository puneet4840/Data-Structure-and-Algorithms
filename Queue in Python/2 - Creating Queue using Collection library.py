# Creating Queue using collection.dequeue class.
print()

from collections import deque

q=deque()

q.append(10)
q.append(20)
q.append(30)

print(f"Queue:")
for item in q:
    print(item,end=" ")


q.popleft()
print()

for item in q:
    print(item,end=" ")