import sys
input = sys.stdin.readline

def query(start,end,idx,left,right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
    return query(start,mid,idx*2,left,right) + query(mid+1,end,idx*2+1,left,right)

def rewrite(start,end,idx,node):
    if node < start or node > end:
        return 
    tree[idx] += 1
    if start == end:
        return 
    mid = (start + end) // 2
    rewrite(start,mid,idx*2,node)
    rewrite(mid+1,end,idx*2+1,node)

n,m = map(int,input().split())

arr = {}
arr2 = {}
for i in range(n):
    a,b = map(int,input().split())
    arr[a] = b
    arr2[b] = a
tree = [0] * (len(arr)*4)

cnt = 0
for i in range(n):
    idx = arr2[arr[i]]
    cnt += query(0,n,1,idx,n)
    rewrite(0,n-1,1,idx-1)
print(cnt)