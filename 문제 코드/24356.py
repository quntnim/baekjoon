a,b,c,d = map(int,input().split())
n,m = a*60+b,c*60+d
if n > m: m+=24*60
print(m-n,(m-n)//30)