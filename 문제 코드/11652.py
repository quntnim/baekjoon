import sys
from collections import Counter
input = sys.stdin.readline

n = int(input());arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
c = Counter(arr)
m = c.most_common(1)
print(m[0][0])