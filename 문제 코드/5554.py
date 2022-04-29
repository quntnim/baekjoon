arr = []
for i in range(4):
    arr.append(int(input()))
if(sum(arr) < 60):
    print('1\n0')
elif(sum(arr)>3599):
    print('59\n59')
else:
    print(sum(arr) // 60), print(sum(arr) % 60)