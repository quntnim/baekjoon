a = int(input())
arr = list(map(float,input().split()))
res = 0
for i in arr:
    res += i**3
print(f'{res ** (1/3)}')