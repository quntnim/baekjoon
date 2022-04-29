arr = list(map(int,input().split()))
if(sum(arr) >= 100):print('OK')
else:
    if(arr[0] == min(arr)):print('Soongsil')
    elif(arr[1] == min(arr)):print('Korea')
    else:print('Hanyang')