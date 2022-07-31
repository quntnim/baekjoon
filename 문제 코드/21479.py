import functools
result = [];tf = False
arr = []
while True:
    try:
        arr.append(input())
    except:
        break
arr = sorted(arr,
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
for i in range(len(arr)):
    if(arr[i] == big and not tf):
        result.append(arr[i])
        tf = True
    else:
        result.append(arr[i])
    
if result[0]=='0':
    print(0)
else:
    print("".join(result))