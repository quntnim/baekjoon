s = input()
c = input()
for i in s:
    if i in c: 
        print(i.swapcase(),end='')
    else: print(i,end='')