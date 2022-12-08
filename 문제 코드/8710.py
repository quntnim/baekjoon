import math
n,w,a = map(int,input().split())
if w <= n:print(0)
else:print(math.ceil((w-n)/a))