import math
n1, n2 = map(int,input().split())
je = []
nj = []
na = []

def issquare(n):
    if(n == 1):
        return False
    else:
        return int(n ** 0.5) ** 2 == n

for i in range(n1 ,n2 + 1):
    if(issquare(i)):
        je.append(i)
    else:
        nj.append(i)

for i in nj:
    for j in je:
        if(i % j == 0):
            na.append(i)
            
tmp = nj
for i in na:
    if(nj.__contains__(i)):
        tmp.remove(i)

print(len(tmp))