s=list(input().split())
c=0
for x in s:
    if s.count(x)>1:c=1
print('no'if c else'yes')