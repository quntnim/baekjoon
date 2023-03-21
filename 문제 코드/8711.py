n = int(input())
arr = list(map(int,input().split()))
x = []
for i in range(n-1):
    if arr[i] > arr[i+1]:
print(x)