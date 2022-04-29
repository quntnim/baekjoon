import math
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr
arr = is_prime(123456*2)
while True:
    cnt = 0
    n = int(input())
    if n == 0:break
    elif n == 1:cnt+=1
    else:
        for i in range(n+1, n*2):
            if arr[i] == True:cnt+=1
    print(cnt)