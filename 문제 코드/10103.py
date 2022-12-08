cy, sd = 100, 100
for i in range(int(input())):
    a,b = map(int,input().split())
    if a > b: sd -= a
    elif b > a: cy -= b
print(cy)
print(sd)
