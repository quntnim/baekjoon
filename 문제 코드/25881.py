n,d = map(int,input().split())
arr = []
for _ in range(int(input())):
    arr.append(int(input()))
for i in arr:
    print(i,end=' ')
    print(i*n if i <= 1000 else 1000*n + d*(i-1000))