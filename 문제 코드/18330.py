n = int(input())
k = int(input()) + 60
if n <= k:
    print(n*1500)
else:
    print(k*1500+(n-k)*3000)