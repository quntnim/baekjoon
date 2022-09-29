arr = []
for i in range(8):
    arr.append(list(input()))
cnt = 0
for i in range(8):
    cnt += arr[i][i%2::2].count('F')
print(cnt)