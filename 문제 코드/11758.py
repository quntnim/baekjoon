p = []
for i in range(3):
    a,b = map(int,input().split())
    p.append([a,b])

def ccw(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

res = ccw(p[0],p[1],p[2])
if res > 0 :print(1)
elif res < 0:print(-1)
else:print(0)