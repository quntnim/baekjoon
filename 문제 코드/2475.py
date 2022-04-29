arr = list(map(int, input().split()))
sum = 0
for i in range(0, 5):
    sum += (arr[i]*arr[i])
print(sum % 10)