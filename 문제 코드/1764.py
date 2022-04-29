import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
nohear = [];cnt = 0;c=[]
for _ in range(n):
    nohear.append(input().rstrip())
for _ in range(m):
    nohear.append(input().rstrip())

nohearsee = Counter(nohear)
for key,value in nohearsee.items():
    if value == 2:cnt+=1;c.append(key)
c.sort()
print(cnt)
for i in range(cnt):
    print(c[i])