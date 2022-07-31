import sys
input = sys.stdin.readline

while True:
    n=int(input())
    g = 0
    if n == 0:
        break
    p=list(map(int,input().split()))
    for i in p:
        g ^= i
    if g==0:
        print(0)
    else:
        cnt = 0
        for i in p:
            if g^i<i:cnt+=1
        print(cnt)