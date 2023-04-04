p1,s1 = map(int,input().split())
s2,p2 = map(int,input().split())
res = ''
if p1+p2 == s1+s2:
    if p1 == s2:res = 'Penalty'
    elif p1 > s2:
        res = 'Esteghlal'
    else:
        res = 'Persepolis'
else:
    if p1+p2 > s1+s2:res = 'Persepolis'
    else:res = 'Esteghlal'
print(res)