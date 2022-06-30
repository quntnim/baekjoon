import math
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr

n,m = map(int,input().split())
arr = is_prime(10000000)
for i in range(n,m):
    if str(i) == str(i)[::-1]:
        if arr[i]:
            print(i)
print(-1)