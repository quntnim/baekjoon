arr = []
for _ in range(int(input())):
    arr.append(input().split())
arr.sort(key=lambda a: int(a[0]))
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])