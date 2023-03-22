x = int(input())
y = int(input())
h = int(input())
if max(x,y) // min(x,y) <= 2:
    if min(x,y) // h>= 2:
        print('good')
        exit()
print('bad')