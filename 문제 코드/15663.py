from itertools import *
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
res = list(combinations_with_replacement(arr,m))
check = set()
for i in res:
    if i not in check:
        print(' '.join(map(str,i)))
        check.add(i)