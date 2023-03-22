s = input()
res = ''
i = 0
while 1:
    try:res += s[i]
    except:break
    i += ord(s[i])-64
print(res)