arr = [0,0,0,0,0]
for i in range(int(input())):
    x,y = map(int,input().split())
    if x==0 or y==0:arr[4]+=1
    elif x>0 and y>0:arr[0]+=1
    elif x<0 and y>0:arr[1]+=1
    elif x<0 and y<0:arr[2]+=1
    else:arr[3]+=1 
for i in range(4):print(f'Q{i+1}:',arr[i])
print('AXIS:',arr[4])