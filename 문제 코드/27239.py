n = int(input())
print(['a','b','c','d','e','f','g','h'][(n%8)-1] + f'{((n-1)//8)+1}')