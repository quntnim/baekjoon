a,c,e = map(int,input().split())
x,y,z = map(int,input().split())
res = 'E'
if z >= e:
    if y >= c:
        if x >= a:res = 'A'
        elif x >= a/2:res = 'B'
        else:res = 'C'
    elif y >= c/2:res = 'D'
    else:res = 'E'
print(res)