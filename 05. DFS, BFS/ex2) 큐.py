#ex2) 큐, 129p

from collections import deque
queue = deque()

queue.append(5) #5
queue.append(2) #52
queue.append(3) #523
queue.append(7) #5237
queue.popleft() #237
queue.append(1) #2371
queue.append(4) #23714
queue.popleft() #3714

print(queue)
queue.reverse()
print(queue)
