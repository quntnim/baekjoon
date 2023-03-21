n = int(input())
res = 25+1*n/100
if res < 100: res = 100
if res > 2000: res = 2000
print(f'{res:.2f}')