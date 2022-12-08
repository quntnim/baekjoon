a,b = map(int,input().split())
if not a%2 or not b%2:print(0)
else:print(min(a,b))