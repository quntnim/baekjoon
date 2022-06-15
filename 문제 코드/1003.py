import sys
input=sys.stdin.readline

arr =[0,1] + [0]*123
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fibo(n-1) + fibo(n-2)
        return arr[n]
        
for _ in range(int(input())):
    n=int(input())
    fibo(n)
    if n == 0:
        print('1 0')
    else:
        print(arr[n-1],arr[n])