for i in range(int(input())):
    a,b = map(int,input().split())
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(a//b,a%b))