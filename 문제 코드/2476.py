res = []
for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a == b and b == c and c == a:res.append(10000+a*1000)
    elif a == b and b != c:res.append(1000+a*100)
    elif b == c and b != a:res.append(1000+b*100)
    elif c == a and a != b:res.append(1000+c*100)
    else:res.append(max(a,b,c)*100)
print(max(res))

