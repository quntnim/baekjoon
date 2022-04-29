import sys
input = sys.stdin.readline

def fail(pt):
    lp=len(pt)
    t=[0]*lp
    i=0

    for j in range(1,lp):
        while i>0 and pt[i]!=pt[j]:
            i=t[i-1]
        if pt[i]==pt[j]:
            i+=1
            t[j]=i
    return t


l = int(input())
s = input().rstrip()
n = fail(s)
print(l - n[l - 1])