n = int(input())
res = []
for m in range(1000000):
    t = m
    for i in str(m):
        t += int(i)
    if t==n:
        res.append(m)
try:
    print(min(res))
except:print(0)