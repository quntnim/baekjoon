arr = []
arr2 = []
for i in range(4):
    arr.append(int(input()))
for i in range(2):
    arr2.append(int(input()))
arr.sort()
arr2.sort()
print(sum(arr[1::])+arr2[-1])