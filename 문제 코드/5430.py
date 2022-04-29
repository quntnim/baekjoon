from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    command = list(input())
    n = int(input())
    check = True
    r = 0
    try:
        arr = deque(map(int,input().rstrip().strip('['']').split(',')))
    except:
        arr = []
    for i in command:
        if i == 'R':
            if r == 0: r = 1
            else: r = 0
        elif i =='D':
            if r == 0:
                if len(arr) == 0:print('error');check = False;break
                else:arr.popleft()
            else:
                if len(arr) == 0:print('error');check = False;break
                else:arr.pop()

    if check:
        if r == 0:print('[' + ','.join(map(str,arr))+ ']')
        else:print('[' + ','.join(map(str,reversed(arr)))+ ']')