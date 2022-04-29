import sys
from collections import Counter
inp = sys.stdin.readline
n = int(inp());arr = [int(inp()) for _ in range(n)]
arr.sort()
print(round(sum(arr) / n))
print(arr[n // 2])
c = Counter(arr).most_common(2)
try:
    if c[0][1] == c[1][1]:print(c[1][0])
    else: print(c[0][0])
except:
    print(c[0][0])
print(max(arr)-min(arr))