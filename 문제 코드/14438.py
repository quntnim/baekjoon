import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
tree = [0] * (len(arr)*4)

def segtree(start,end,idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2

    l = segtree(start,mid,idx*2)
    r = segtree(mid+1,end,idx*2+1)

    tree[idx] = min(l,r)
    return tree[idx]

def isum(start,end,idx,left,right):
    if left > end or right < start: return 10**9+1
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
   
    l = isum(start,mid,idx*2,left,right)
    r = isum(mid+1,end,idx*2+1,left,right)
    return min(l,r)

def rewrite(start,end,idx,node,val):
    if node < start or node > end:
        return tree[idx]
    tree[idx] += val
    if start != end:
        mid = (start + end) // 2
        l = rewrite(start,mid,idx*2,node,val)
        r = rewrite(mid+1,end,idx*2+1,node,val)
        tree[idx] = min(l,r)
    return tree[idx]

segtree(0, len(arr) - 1, 1)

for _ in range(int(input())):
    a,b,c = map(int,input().rstrip().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        rewrite(0,len(arr) - 1,1,b-1,diff)
    if a == 2:
        print(isum(0,len(arr) - 1,1,b-1,c-1))