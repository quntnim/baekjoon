L, P = map(int, input().split())
arr = list(map(int, input().split()))
sum = L * P
for i in range(0, 5):
    print(arr[i] - sum, end=' ')
print()