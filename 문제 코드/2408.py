s = ''
for i in range(int(input())*2-1):
    t = input()
    if t == '/':t='//'
    s += t
print(eval(s))