import math
import sys
input = sys.stdin.readline
def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr

arr = is_prime(10000001)
while 1:
    try:
        m, n = map(int,input().split())
    except:
        break
    input()
    cnt = 0
    for i in range(m, n+1):
        if arr[i] == True:
            cnt+=1
    print(cnt)
    print()