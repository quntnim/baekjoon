import sys
input = sys.stdin.readline

def psum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def query(start, end):
    return psum(end) - psum(start - 1)

def rewrite(idx,val):
    while idx < len(tree):
        tree[idx] += val
        idx += (idx & -idx)

for _ in range(int(input())):
    n = int(input())

    tree = [0] * (n+1)
    arr = list(map(int,input().split()))
    arr2 = {}
    value = list(map(int,input().split()))
    for i in range(n):
        arr2[value[i]] = i+1

    cnt = 0
    for i in range(n):
        idx = arr2[arr[i]]
        cnt += query(idx,n)
        rewrite(idx,1)
    print(cnt)