n = int(input());arr = []
for _ in range(n):arr.append(list(map(int,input().split())))
for i in range(n):arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
arr.sort()
for i in range(n):print(arr[i][1], arr[i][0])