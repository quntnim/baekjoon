def lucas(x, z):
    a = 1
    if x < z:return 0
    elif x == z:return 1
    for i in range(1, z + 1):
        a = (a*(x-i+1))//i
    return a

n,r,m= map(int, input().split())
narr = [];karr = []
while n or r:
    narr.append(n % m);karr.append(r % m)
    n //= m;r //= m
    
res = 1
for i in range(len(narr)):
    res *= lucas(narr[i], karr[i])
    res %= m
print(res)