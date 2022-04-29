a = list(map(int,input().split())); count = 0;arr = []
for i in range (min(a)+1 ,max(a)):arr.append(i);count +=1
print(count)
for l in arr:print(l,end=' ')