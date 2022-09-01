for i in range(int(input())):
    arr = list(map(int,input().split()))
    arr[0] **= 2;arr[1] **= 2;arr[2] **= 2
    arr.sort()
    print(f'Scenario #{i+1}:')
    print('yes'if arr[0] + arr[1] == arr[2] else'no')
    print()