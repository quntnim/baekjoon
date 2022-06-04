while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a == 0:
        print("{0} {1} {2}".format(c//b,b,c))
    if b == 0:
        print("{0} {1} {2}".format(a,c//a,c))
    if c == 0:
        print("{0} {1} {2}".format(a,b,a*b))