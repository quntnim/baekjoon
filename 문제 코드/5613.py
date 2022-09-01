cmd = []
while True:
    temp = input()
    if temp == '=':break
    if temp == '/':temp = '//'
    cmd.append(temp)

s = ''.join(cmd[:3])
res = eval(s)
for i in range(3,len(cmd),2):
    s = f''.join(cmd[i:i+2])
    res = eval(str(res) + s)
print(res)