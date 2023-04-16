import sys
input=sys.stdin.readline

def kmp(pat,txt):
    result=[]
    lt=len(txt)
    lp=len(pat)
    table=mk_table(pat)
    i=0
    for j in range(lt):
        while i>0 and pat[i]!=txt[j]:
            i=table[i-1]
        if pat[i]==txt[j]:
            if i==lp-1:
                result.append(j-lp+2)
                i=table[i]
            else:
                i+=1
    return result

def mk_table(P):
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

s1=input().rstrip()
s2=input().rstrip()
s2+=s2
print(len(kmp(s1,s2[:-1])))