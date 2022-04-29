d = list(map(int,input().split()))
if(d[0] == d[1] == d[2]):
    print(10000+d[0]*1000)
elif(d[0] == d[1] or d[0] == d[2]):
    print(1000+d[0]*100)
elif(d[1] == d[2]):
    print(1000+d[1]*100)
else:
    print(max(d)*100)