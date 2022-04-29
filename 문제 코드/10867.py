input()
n = list(map(int,input().split()));n = list(set(n));n.sort()
for i in n:
    print(i,end=' ')