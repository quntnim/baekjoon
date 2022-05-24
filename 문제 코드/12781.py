x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())

a,b,c,d = [x1,y1],[x2,y2],[x3,y3],[x4,y4]
def ccw(a,b,c):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

if ccw(a,b,c)*ccw(a,b,d) < 0 and ccw(c,d,a)*ccw(c,d,b) < 0:
    print(1)
else:
    print(0)