arr = []
for i in range(int(input())):
    a,b = map(int,input().split())
    if a<=b:arr.append(b)
print(min(arr) if arr else -1)