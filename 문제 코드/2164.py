from collections import deque
n = int(input())
arr = deque(i for i in range(1,n+1))
while True:
    if len(arr) == 1:break
    else: 
        arr.popleft()
        arr.append(arr.popleft())
print(arr[0])