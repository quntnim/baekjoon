l = int(input())
n = int(input())
if n-l > 30:c = 500
elif 30 >= n-l > 20:c = 270
elif 20 >= n-l > 0:c = 100
else:c=0
print(f'You are speeding and your fine is ${c}.'if c else'Congratulations, you are within the speed limit!')