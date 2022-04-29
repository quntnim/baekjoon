import sys
m = int(sys.stdin.readline());s = set()

for _ in range(m):
    a = sys.stdin.readline().strip().split()
    if len(a) == 1:
        if(a[0] == 'all'):
            s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        elif(a[0] == 'empty'):s = set()

    else:
        n = int(a[1])
        if(a[0] == 'add'):s.add(n)
        elif(a[0] == 'check'):
            if(n in s): print(1)
            else: print(0)
        elif(a[0] == 'remove'):s.discard(n)
        elif(a[0] == 'toggle'):
            if(n in s):s.discard(n)
            else: s.add(n)