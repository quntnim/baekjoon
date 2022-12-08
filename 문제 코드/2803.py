while 1:
    n,a,w = input().split()
    if n == '#' and a == '0' and a == w:
        break
    print(f'{n} Senior'if int(a)>17 or int(w)>=80 else f'{n} Junior')