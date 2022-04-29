from itertools import *
import sys
input = sys.stdin.readline
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    res = list(combinations(arr[1::], 6))
    res = set(res);res = list(res)
    res.sort()
    check = set()
    for i in res:
        if i not in check:
            print(' '.join(map(str,i)))
            check.add(i)
    print()