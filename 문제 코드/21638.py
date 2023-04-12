t,v = map(int,input().split())
a,b = map(int,input().split())
if a < 0 and b >= 10:
    print('A storm warning for tomorrow! Be careful and stay home if possible!')
elif t > a:
    print('MCHS warns! Low temperature is expected tomorrow.')
elif v < b:
    print('MCHS warns! Strong wind is expected tomorrow.')
else:
    print('No message')