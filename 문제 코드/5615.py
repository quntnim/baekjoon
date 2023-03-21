import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
        
    def miller_rabin(n,b):
        s = 0
        t = n-1
        while t%2 == 0:
            s += 1
            t = t // 2
        x = pow(b,t,n)
        if x == 1 or x == n-1:
            return True
        for _ in range(0,s-1):
            x = pow(x,2,n)
            if x == n-1:
                return True
        return False
        
    check = 0
    for i in [2,3,5,7,11]:
        if not miller_rabin(2*n+1,i):break
        else:check+=1
    if check == 5:
        return True
    else:
        return False

cnt = 0
n = int(input())
for i in range(n):
    m = int(input())
    if is_prime(m):cnt+=1
print(cnt)