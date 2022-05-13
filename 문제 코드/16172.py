import re
import sys
input = sys.stdin.readline

def kmp(txt,pat):
    lt=len(txt)
    lp=len(pat)
    table=fail(pat)
    i=0
    for j in range(lt):
        while i>0 and pat[i]!=txt[j]:
            i=table[i-1]
        if pat[i]==txt[j]:
            if i==lp-1:
                return 1
            else:
                i+=1
    return 0

def fail(P):
    lp=len(P)
    t=[0]*lp
    i=0
    for j in range(1,lp):
        while i>0 and P[i]!=P[j]:
            i=t[i-1]
        if P[i]==P[j]:
            i+=1
            t[j]=i
    return t

s = input().rstrip();p=input().rstrip()
s = re.sub(r'[0-9]+','',s)
print(kmp(s,p))