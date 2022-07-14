a,b = map(int,input().split())
arr = []
arr2 = []
cnt = 0
for i in range(a):
    arr.append(input())
input()
for i in range(a):
    arr2.append(input())
for y in range(a):
    for x in range(b):
        if arr[y][x] == arr2[y][x] : cnt +=1
print(cnt)