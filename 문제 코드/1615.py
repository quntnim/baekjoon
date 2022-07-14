import sys
input = sys.stdin.readline

def psum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def query(start, end):
    return psum(end) - psum(start)

def rewrite(idx,val):
    while idx < len(tree):
        tree[idx] += val
        idx += (idx & -idx)

n,m = map(int,input().split())

tree = [0] * (n+1)
arr = []
for i in range(m):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()

cnt = 0
for i in range(m):
    idx = arr[i][1]
    cnt += query(idx,n)
    rewrite(idx,1)
print(cnt)