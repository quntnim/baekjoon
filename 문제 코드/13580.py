arr = list(map(int,input().split()))
arr.sort()
check = False
if arr[0]+arr[1]==arr[2]:check = True
elif arr[0]==arr[1] or arr[1]==arr[2] or arr[2]==arr[0]:check = True
print('NS'[check])