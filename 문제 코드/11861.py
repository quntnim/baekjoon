import sys
sys.setrecursionlimit(10**6)

def segtree(start,end,idx):
    if start == end:
        tree[idx] = start
        return tree[idx]
    mid = (start + end) // 2
    l = segtree(start,mid,idx*2)
    r = segtree(mid+1,end,idx*2+1)
    if arr[l] < arr[r]:
        tree[idx] = l
    else:
        tree[idx] = r
    return tree[idx]

def query(start,end,idx,left,right):
    if left > end or right < start: return -1
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
    l = query(start,mid,idx*2,left,right)
    r = query(mid+1,end,idx*2+1,left,right)
    if l == -1 or r == -1:
        return max(l,r)
    else:
        if arr[l] < arr[r]:
            return l
        else:
            return r

def result(start,end):
    if start == end:return arr[start]
    min_idx = query(0,n-1,1,start,end)
    temp = (end-start+1)*arr[min_idx]
    if min_idx > start: temp = max(temp,result(start,min_idx-1))
    if min_idx < end: temp = max(temp,result(min_idx+1,end))
    return temp

n = int(input())
arr = list(map(int,input().split()))
tree = [0] * (n*4)
segtree(0, n-1, 1)
print(result(0,n-1))