import sys
input = sys.stdin.readline

def segtree(start,end,idx):
    if start == end:
        tree[idx] = start
    else:
        mid = (start + end) // 2

        segtree(start,mid,idx*2)
        segtree(mid+1,end,idx*2+1)

        if arr[tree[idx*2]] <= arr[tree[idx*2+1]]:
            tree[idx] = tree[idx*2]
        else:
            tree[idx] = tree[idx*2+1]

def query(start,end,idx):
    left = start
    right = end
    if left > end or right < start: return -1
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
   
    l = query(start,mid,idx*2,left,right)
    r = query(mid+1,end,idx*2+1,left,right)
    if l == -1:
        return r
    elif r == -1:
        return l
    else:
        if arr[l]<=arr[r]:
            return l
        else:
            return r

def rewrite(start,end,idx,node,val):
    if node < start or node > end:
        return tree[idx]
    if start == end:
        tree[idx] = node
        return
    
    mid = (start + end) // 2
    rewrite(start,mid,idx*2,node,val)
    rewrite(mid+1,end,idx*2+1,node,val)
    if arr[tree[idx*2]] <= arr[tree[idx*2+1]]:
        tree[idx] = tree[idx*2]
    else:
        tree[idx] = tree[idx*2+1]

n = int(input())
arr = list(map(int,input().split()))
tree = [0] * (len(arr)*4)
segtree(0, len(arr) - 1, 1)

for _ in range(int(input())):
    com = list(input().split())
    if com[0] == '1':
        b = int(com[1])
        c = int(com[2])
        diff = c - arr[b-1]
        arr[b-1] = c
        rewrite(0,len(arr) - 1,1,b-1,diff)
    if com[0] == '2':
        print(query(0,len(arr) - 1,1)+1)