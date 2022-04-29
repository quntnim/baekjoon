import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp());que = deque()
for i in range(n):
    c = inp().split();
    try:
        n = int(c[1])
    except:
        n=0
    if c[0] == 'push_back' : que.append(n)
    if c[0] == 'push_front' : que.appendleft(n)
    elif c[0] == 'pop_front' : 
        try:
            print(que.popleft())
        except:
            print(-1)
    elif c[0] == 'pop_back' : 
        try:
            print(que.pop())
        except:
            print(-1)
    elif c[0] == 'size' : print(len(que))
    elif c[0] == 'empty' :
        if len(que) == 0 : print(1)
        else : print(0)
    elif c[0] == 'front' :
        try:
            print(que[0])
        except:
            print(-1)
    elif c[0] == 'back' :
        try:
            print(que[-1])
        except:
            print(-1)