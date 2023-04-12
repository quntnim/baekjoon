res = 0
for _ in range(4):
    t,s = input().split()
    s=int(s)
    if t == 'Es':res+=s*21
    else:res+=s*17
print(res)