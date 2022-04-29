arr = list(input())
eng = 'abcdefghijklmnopqrstuvwxyz'
for e in eng:
    try:
        print(arr.index(e),end=' ')
    except:
        print('-1',end=' ')