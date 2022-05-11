import sys
input = sys.stdin.readline
n, cap = map(int,input().rstrip().split())
size = [];val = []

for i in range(n):
    a, b = map(int,input().rstrip().split())
    size.append(a)
    val.append(b)

def knapsack(cap, n):
    arr = [[0 for _ in range(cap+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for s in range(1, cap+1):
            if size[i-1] > s:
                arr[i][s] = arr[i-1][s]
            else:
                arr[i][s] = max(val[i-1] + arr[i-1][s-size[i-1]], arr[i-1][s])
    return arr[n][cap]

print(knapsack(cap,n))