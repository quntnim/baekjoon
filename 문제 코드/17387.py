x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

a,b,c,d = [x1,y1],[x2,y2],[x3,y3],[x4,y4]
def ccw(a,b,c):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

L = ccw(a,b,c)*ccw(a,b,d); R = ccw(c,d,a)*ccw(c,d,b)
if L <= 0 and R <= 0:
    if L == 0 and R == 0:
        if max(a[0],b[0]) >= min(c[0],d[0]) and max(c[0],d[0]) >= min(a[0],b[0]) and max(a[1],b[1]) >= min(c[1],d[1]) and max(c[1],d[1]) >= min(a[1],b[1]):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)