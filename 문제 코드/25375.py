import sys
input = sys.stdin.readline
for i in range(int(input())):
    a,b = map(int,input().split())
    print(1 if a*2<=b and b%a==0 else 0)