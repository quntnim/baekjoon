a,b = map(int,input().split())
c,d = map(int,input().split())
sun = b-a
moon = d-c
for i in range(5001):
    sun-=1
    moon-=1
    if not sun and not moon:
        print(i+1)
        break
    elif not sun and moon:sun+=b
    elif sun and not moon:moon+=d