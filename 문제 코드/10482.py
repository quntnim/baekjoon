import sys
import math
input = sys.stdin.readline

def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr

arr = is_prime(32000)

for _ in range(int(input())):
    cnt = 0
    res = []
    n = int(input())
    for i in range(3,n//2+1):
        if arr[i] and arr[n-i]:
            cnt+=1
            res.append([i,n-i])
    if n == 4:
        print("4 has 1 representation(s)")
        print("2+2")
    else:
        print("{0} has {1} representation(s)".format(n,cnt))
        for i in res:
            print("{0}+{1}".format(i[0],i[1]))
    print()