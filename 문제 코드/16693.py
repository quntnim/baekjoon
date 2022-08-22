import math
a,b = map(int,input().split())
c,d = map(int,input().split())
c=(c**2) * math.acos(-1)
print('Slice of pizza' if a/b > c/d else 'Whole pizza')