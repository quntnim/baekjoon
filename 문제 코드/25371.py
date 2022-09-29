def change(n, a):
    res = ''
    while n > 0:
        n, mod = divmod(n, a)
        res += str(mod)
    return res[::-1] 

a,b = map(int,input().split())
temp = change(a,b).split('0')
res = 0
for i in temp:
    if i == '':continue
    res += int(i)
print(change(res,b))