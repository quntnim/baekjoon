arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
for i in arr[:8]:
    print(i)
