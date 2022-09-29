input()
arr = list(map(int,input().split()))
now = 0
res = 0
arr.sort()
for i in arr:
    now += i
    res += now
print(res)