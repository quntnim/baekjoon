n = int(input());cnt = 0
money = [500,100,50,10,5,1]
paid = 1000 - n
left = paid
for i in money:
    if i <= paid:
        while True:
            if i > left:break
            else: left -= i;cnt+=1  
    if left == 0:break
print(cnt)