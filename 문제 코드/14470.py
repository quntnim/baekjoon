a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
time = 0
if a==0:
    time+=d
    time+=e*(b-a)
elif a<0:
    time+=c*(-a)
    time+=d
    time+=e*(b)
else:
    time+=e*(b-a)
print(time)