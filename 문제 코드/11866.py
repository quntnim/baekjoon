n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
k-=1
t=0
print('<',end='')
while(len(arr) != 1):
    t+=k
    t%=n
    print(arr[t],end=', ')
    arr.pop(t)
    n-=1
print(arr[0],end='')
print('>',end='')
