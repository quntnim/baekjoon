import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
result = [0]
for i in range(n):
    result.append(result[i] + arr[i])
for i in range(m):
    a,b = map(int,input().split())
    print(result[b] - result[a-1])