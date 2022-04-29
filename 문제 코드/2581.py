import math
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr
m = int(input());n = int(input())
arr = is_prime(n)
num = []
for i in range(m, len(arr)):
    if arr[i] == True:num.append(i)
if len(num) == 0:
    print(-1)
else:
    print(sum(num));print(min(num))