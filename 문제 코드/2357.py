import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
tree = [0] * (len(arr)*4)

def segtree(start,end,idx):
    if start == end:
        tree[idx] = (arr[start],arr[start])
        return tree[idx]
    mid = (start + end) // 2

    l = segtree(start,mid,idx*2)
    r = segtree(mid+1,end,idx*2+1)

    tree[idx] = (min(l[0],r[0]), max(l[1],r[1]))
    return tree[idx]

def isum(start,end,idx,left,right):
    if left > end or right < start: return (1000000000,0)
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2

    l = isum(start,mid,idx*2,left,right)
    r = isum(mid+1,end,idx*2+1,left,right)

    return (min(l[0],r[0]), max(l[1],r[1]))

segtree(0, len(arr) - 1, 1)

for _ in range(m):
    a,b= map(int,input().split())
    print(*isum(0,len(arr)-1,1,a-1,b-1))