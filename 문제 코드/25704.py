n = int(input())
p = int(input())
if n >= 20:res = min(int(p*0.75),p-2000)
elif n >= 15:res = min(int(p*0.9),p-2000)
elif n >= 10:res = min(int(p*0.9),p-500)
elif n >= 5:res = p-500
else:res = p
print(0 if res < 0 else res)