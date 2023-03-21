import sys
input = sys.stdin.readline

def is_prime(n):
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
            x = x*x%n
            if x == n-1:
                return True
        return False

    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
        
    for i in [2,3,5,7,11,13,17]:
        if n == i: return True
        if not miller_rabin(n,i):return False
    return True

def palindrome(a):
    t=a
    a//=10
    while a > 0:
        t*=10 
        t+=a%10
        a//= 10
    return t

pdprime = [2,3,5,7,11]
l,h = map(int,input().split())
cnt = 0
for i in range(10,1234567):
    t = palindrome(i)
    if is_prime(t):pdprime.append(t)

for i in pdprime:
    if i > h:
        break
    if i >= l:
        cnt+=1
print(cnt)