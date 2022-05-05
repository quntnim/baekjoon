a,b,c=map(int,input().split())
print(a*b//c if b>c else a*c//b)