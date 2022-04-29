import sys
p=sys.stdin.readline
for i in range(int(p())):
 c=0
 for l in map(int,p().split()):
  if l%2==1:c+=1
 if c==3 or c==2:print('B')
 elif c==0 or c==1:print('R')