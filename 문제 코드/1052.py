a,b=map(int,input().split());c = 0
while bin(a).count('1')>b:
    l=bin(a)[::-1].index('1')
    c+=2**l;a+=2**l
print(c)