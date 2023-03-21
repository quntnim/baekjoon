arr = []
for i in range(4):
    arr.append(list(map(int,input().split())))

print(arr)
print([*zip(*arr)])