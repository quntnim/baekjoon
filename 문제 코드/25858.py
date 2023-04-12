n,d = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in arr:
    print((d//sum(arr))*i)