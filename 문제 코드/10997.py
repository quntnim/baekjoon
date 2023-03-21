a = int(input())
arr = [['' for _ in range(a*2+1)]for _ in range(a*3 + a-1)]

def star(n,x,y):

    for _ in range(n*4-4):
        arr[y][x] = '*'
        x-=1
        print(y,x)
    for y in range(n*4-2):
        arr[y][x] = '*'
        y+=1
        print(y,x)
    for _ in range(n*4-4):
        arr[y][x] = '*'
        x+=1
        print(y,x)
    for _ in range(n*4-4):
        arr[y][x] = '*'
        y+=1
        print(y,x)
star(a,a*2,0)
print(arr)