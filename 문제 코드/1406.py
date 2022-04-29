import sys;p=sys.stdin.readline;a=list(p().strip());b=[];l=a.append
for i in range(int(p())):
 c=p().strip().split()
 if c[0]=='L'and a:b.append(a.pop())
 if c[0]=='D'and b:l(b.pop())
 if c[0]=='B'and a:a.pop()
 if c[0]=='P':l(c[1])
print(''.join(a+b[::-1]))