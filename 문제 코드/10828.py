import sys
inp = sys.stdin.readline
n = int(inp());stack = []
for i in range(n):
    c = inp().split();
    try:
        n = int(c[1])
    except:
        n=0
    if c[0] == 'push' : stack.append(n)
    elif c[0] == 'pop' : 
        try:
            print(stack.pop())
        except:
            print(-1)
    elif c[0] == 'size' : print(len(stack))
    elif c[0] == 'empty' :
        if len(stack) == 0 : print(1)
        else : print(0)
    elif c[0] == 'top' :
        try:
            print(stack[-1])
        except:
            print(-1)