from collections import deque
n,q = map(int,input().split());back=deque();front=deque();now='null'

for i in range(q):
    command = input().split()
    if command[0] == 'A':
        if now == 'null':
            now = command[1]
            front.clear()
        else: 
            back.append(now)
            now = command[1]
            front.clear()
    if command[0] == 'B':
        if len(back) > 0:
            front.append(now)
            now = back.pop()
    if command[0] == 'F':
        if len(front) > 0:
            back.append(now)
            now = front.pop()
    if command[0] == 'C':
        tmp = 0
        if len(back) >= 2:
            for i in range(len(back)-1, -1, -1):
                if back[i] == tmp:
                    del back[i]
                else: tmp = back[i]
print(now)
if len(back) == 0:
    print(-1)
else:
    print(*reversed(back))

if len(front) == 0:
    print(-1)
else:
    print(*reversed(front))