import math
for i in range(int(input())):
    a,p1 = map(int,input().split())
    r,p2 = map(int,input().split())
    print("Slice of pizza"if a/p1 > (math.pi*r*r)/p2 else"Whole pizza")