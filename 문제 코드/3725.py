import sys,re
sys.setrecursionlimit(20000)
s = list(filter(None,re.split("([-|+|*|/|(|)])",input())))
check = False
rock = False
for i in range(len(s)):
    if s[i].isdigit():
        s[i] = str(int(s[i]))
    if s[i] in ['+','-','/','*']:
        if check:
            print('ROCK')
            exit(0)
        else:
            check=True
    else:
        check=False
    if s[i] == '/':
        s[i]='//'
text = ''.join(s)
if '(-'in text or'(+'in text:rock=True
for i in range(10):
    if f"{i}("in text:rock = True
if ")("in text:rock = True
if "()"in text:rock = True
if text[0] in ['+','-','/','*']:
    rock=True
try:
    if rock:
        print('ROCK')
    else:
        print(eval(text))
except:
    print('ROCK')