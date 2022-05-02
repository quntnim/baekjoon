import sys
input=sys.stdin.readline

s=input().rstrip()
def fail(pt):
    lp = len(pt)
    t=[0]*lp
    i=0
    for j in range(1,lp):
        while i>0 and pt[i]!=pt[j]:
            i=t[i-1]
        if pt[i]==pt[j]:
            i+=1
            t[j]=i
    return max(t)

res = []
for i in range(len(s)):
    pt = s[i:]
    res.append(fail(pt))
print(max(res))