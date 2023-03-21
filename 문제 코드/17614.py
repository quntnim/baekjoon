res = 0
for i in range(int(input())+1):
    res += str(i).count('3')+str(i).count('6')+str(i).count('9')
print(res)