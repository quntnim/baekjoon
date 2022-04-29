arr = []
for i in range(5):
    arr.append(int(input()))
    if(arr[i] < 40):
        arr[i] = 40
        
print(sum(arr) // 5)