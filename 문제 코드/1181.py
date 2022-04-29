n = int(input()); arr = []
for i in range(n): arr.append(input())
arr = set(arr);arr = list(arr);arr.sort();arr.sort(key=lambda i : len(i))
for i in range(len(arr)):print(arr[i])