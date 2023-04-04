m,s,g = map(int,input().split())
a,b = map(float,input().split())
l,r = map(int,input().split())

lq = m/g 
if m % g:
    lq+=1
rq = m/s 
if m % s:
    rq+=1

if l/a + lq > r/b + rq:
    print('latmask')
else:
    print('friskus')