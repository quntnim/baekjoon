arr = list(map(int, input().split()))
for i in range(0, 2):
    print(-(arr[i] - 1),end=' ')
for i in range(2, 5):
    print(-(arr[i] - 2),end=' ')
print(-(arr[5] - 8))