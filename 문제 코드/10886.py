tc = int(input())
arr = []
for i in range(tc):
    arr.append(input())
if(arr.count('0') > arr.count('1')):print('Junhee is not cute!')
else:print('Junhee is cute!')