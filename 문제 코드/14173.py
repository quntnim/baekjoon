x1,y1,x2,y2 = map(int,input().split())
a1,b1,a2,b2 = map(int,input().split())
n1,n2,m1,m2 = min(x1,a1),min(y1,b1),max(x2,a2),max(y2,b2)
print(max((m1-n1),(m2-n2))**2)