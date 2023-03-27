a,b,c,d=int(input()),int(input()),int(input()),int(input())
res = 0
if a in [8,9]:res+=1
if d in [8,9]:res+=1
if b==c:res+=1
if res==3:print('ignore')
else:print('answer')