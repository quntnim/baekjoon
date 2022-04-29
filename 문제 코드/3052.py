arr = []
for _ in range(10):
    arr.append(int(input()))
for i in range(10):
    arr[i] %= 42
arr = set(arr)
print(len(arr))