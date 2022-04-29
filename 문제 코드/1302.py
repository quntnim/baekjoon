from collections import Counter
n = int(input());arr=[]
for i in range(n):
    arr.append(input())
arr.sort()
c = Counter(arr)
m = c.most_common(1)
print(m[0][0])