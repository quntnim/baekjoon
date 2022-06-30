import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
tree = [0] * (len(arr)*4)

def segtree(start,end,idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = segtree(start,mid,idx*2) + segtree(mid+1,end,idx*2+1)
    return tree[idx]

def isum(start,end,idx,left,right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
    return isum(start,mid,idx*2,left,right) + isum(mid+1,end,idx*2+1,left,right)

def rewrite(start,end,idx,node,val):
    if node < start or node > end:
        return 
    tree[idx] += val
    if start != end:
        mid = (start + end) // 2
        rewrite(start,mid,idx*2,node,val)
        rewrite(mid+1,end,idx*2+1,node,val)


segtree(0, len(arr) - 1, 1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        rewrite(0,len(arr) - 1,1,b-1,diff)
    if a == 2:
        print(isum(0,len(arr) - 1,1,b-1,c-1))
