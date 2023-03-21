arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
res = 0
for x,y in zip(arr,arr2):
    if y > x:res += y-x
print(res)