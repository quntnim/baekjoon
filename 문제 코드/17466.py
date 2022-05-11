n,p = map(int,input().split())
def fac(n):
    res = 1
    for i in range(2,n+1):
        res = (res*i)%p
    return res
print(fac(n))