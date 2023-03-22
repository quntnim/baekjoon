for i in range(10**6):
    arr = list(map(int,input().split()))
    a = arr[0]
    arr = arr[1:]
    if not a:break
    print(f'Case {i+1}:',end=' ')
    if a%2:print(f'{arr[a//2]:.1f}')
    else:print(f'{(arr[a//2]+arr[a//2-1])/2:.1f}')