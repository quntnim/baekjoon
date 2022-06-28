import math
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr
arr = is_prime(1003002)

n = int(input())
for i in range(n,1003002):
    if str(i) == str(i)[::-1]:
        if arr[i]:
            print(i)
            break