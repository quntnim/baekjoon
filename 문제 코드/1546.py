i=int(input());arr=list(map(int,input().split()));m=max(arr)
for l in range(i):arr[l]=arr[l]/m*100
print(sum(arr)/i)