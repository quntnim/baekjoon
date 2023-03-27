y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())
res = 0
if y1 < y2:
    res = y2-y1-1
    if m2 > m1:
        res = y2-y1
    if m2 == m1:
        res = y2-y1-1
        if d2 >= d1:
            res = y2-y1
print(res)
print(y2-y1+1)
print(y2-y1)