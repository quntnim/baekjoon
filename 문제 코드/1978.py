import math
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr
n = int(input())
numlist = list(map(int,input().split()))
arr = is_prime(max(numlist))
num = [];cnt = 0
for i in range(min(numlist), len(arr)):
    if arr[i] == True:num.append(i)
for i in numlist:
    if i in num:cnt+=1
print(cnt)