cnt = 0
for i in range(6):
    if input() == 'W':cnt+=1
print(1 if cnt in [5,6] else 2 if cnt in [3,4] else 3 if cnt in [1,2] else -1)