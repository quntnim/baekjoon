input();n=list(map(int,input().split()))
n.sort()

def bs(a, t):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start+end) // 2
        if t == a[mid]:return 1
        elif t > a[mid]:start = mid + 1
        else:end = mid - 1
    return 0

input();m=list(map(int,input().split()))
for i in m:
    print(bs(n, i))