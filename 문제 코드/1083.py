import functools
n = int(input()); arr = []; result =[];tf = False
arr = list(map(int,input().split()))
print(arr)
arr = sorted(arr,
key = functools.cmp_to_key
(
    lambda a, b:
    -1 if a < b
    else 1
))
for i in range(len(arr)):
    result.append(arr[i])
print(result)