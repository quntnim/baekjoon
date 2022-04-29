import functools
k, n = map(int,input().split()); arr = []; result =[];tf = False
arr = sorted([input() for _ in range(k)],
key = functools.cmp_to_key
(
    lambda a, b:
    1 if int(a+b) < int(b+a) 
    else -1
))
big = sorted(arr,
key=functools.cmp_to_key
(
    lambda a, b:
    1 if len(a) < len(b) 
    else 0 if len(a) == len(b) and int(a+b) < int(b+a) 
    else -1
))[0]
for i in range(k):
    result.append(arr[i])
    if(arr[i] == big and not tf):
        result.append(arr[i]*(n-k))
        tf = True
print("".join(result))