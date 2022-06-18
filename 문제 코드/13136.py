r,c,n=map(int,input().split())
print((r//n+(1 if r%n>0 else 0))*(c//n+(1 if c%n>0 else 0)))