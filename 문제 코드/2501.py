n,k = map(int,input().split())
arr = []
for i in range(1,n):
    if n%i==0:arr.append(i)
arr.append(n)
try:
    print(arr[k-1])
except:
    print(0)