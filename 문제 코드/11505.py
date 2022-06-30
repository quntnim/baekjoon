import sys
input = sys.stdin.readline

mod = 1000000007
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
    tree[idx] = segtree(start,mid,idx*2) * segtree(mid+1,end,idx*2+1)%mod
    return tree[idx]

def isum(start,end,idx,left,right):
    if left > end or right < start: return 1
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
    return isum(start,mid,idx*2,left,right) * isum(mid+1,end,idx*2+1,left,right)%mod

def rewrite(start,end,idx,node,val):
    if node < start or node > end:
        return 
    if start==end:
        tree[idx] = val
    if start != end:
        mid = (start + end) // 2
        rewrite(start,mid,idx*2,node,val)
        rewrite(mid+1,end,idx*2+1,node,val)
        tree[idx] = tree[idx*2]*tree[idx*2+1]%mod


segtree(0, len(arr) - 1, 1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        arr[b-1]=c
        rewrite(0,len(arr) - 1,1,b-1,c)
    if a == 2:
        print(isum(0,len(arr) - 1,1,b-1,c-1))