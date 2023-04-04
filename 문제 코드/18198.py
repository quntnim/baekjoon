s = input()
a,b = 0,0
for c,n in zip(s[0::2],s[1::2]):
    if c=='A':a+=int(n)
    else:b+=int(n)
if a>b:print('A')
elif b>a:print('B')
