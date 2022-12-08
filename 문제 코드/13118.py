arr = list(map(int,input().split()))
try:print(arr.index(int(list(input().split())[0]))+1)
except:print(0)