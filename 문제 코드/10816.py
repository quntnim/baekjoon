from bisect import bisect_left, bisect_right
n=int(input())
arr=list(map(int,input().split())) + [10000001]
arr.sort()
m=int(input())
arr2=list(map(int,input().split()))
for i in arr2:
    cnt = 0
    t = bisect_left(arr,i)
    if arr[t] == i:
        print(bisect_right(arr,i) - t,end=' ')
    else:
        print(0,end=' ')