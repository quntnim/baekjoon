a = list(map(int,input().split()));b = list(map(int,input().split()))
if(a[0] + b[1] <= a[1] + b[0]): print(a[0]+b[1])
elif(a[1] + b[0] < a[0] + b[1]): print(a[1]+b[0])