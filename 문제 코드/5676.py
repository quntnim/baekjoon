import sys
input = sys.stdin.readline

def conv(n):
    if n==0:return 0
    elif n>0:return 1
    else:return -1

def segtree(start,end,idx):
    if start == end:
        tree[idx] = conv(arr[start])
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = segtree(start,mid,idx*2) * segtree(mid+1,end,idx*2+1)
    return tree[idx]

def isum(start,end,idx,left,right):
    if left > end or right < start: return 1
    if left <= start and right >= end: return tree[idx]
    mid = (start + end) // 2
    return isum(start,mid,idx*2,left,right) * isum(mid+1,end,idx*2+1,left,right)

def rewrite(start,end,idx,node,val):
    if node < start or node > end:
        return 
    if start==end:
        tree[idx] = conv(val)
    if start != end:
        mid = (start + end) // 2
        rewrite(start,mid,idx*2,node,val)
        rewrite(mid+1,end,idx*2+1,node,val)
        tree[idx] = tree[idx*2]*tree[idx*2+1]

while True:
    try:
        n,m = map(int,input().split())
    except:
        break
    arr = list(map(int,input().split()))
    tree = [0] * (len(arr)*4)

    segtree(0, len(arr) - 1, 1)

    for _ in range(m):
        a,b,c = input().split()
        b=int(b)
        c=int(c)
        if a == 'C':
            rewrite(0,len(arr) - 1,1,b-1,c)
        if a == 'P':
            temp = isum(0,len(arr) - 1,1,b-1,c-1)
            if temp == 0:print(0,end='')
            elif temp > 0:print('+',end='')
            else:print('-',end='')
    print()