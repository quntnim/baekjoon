input()
arr=list(map(int,input().split()))
temp=0;res=0
for i in arr:
    if i:temp+=1
    else:temp=0
    res+=temp
print(res)