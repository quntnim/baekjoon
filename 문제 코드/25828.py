g,p,t = map(int,input().split())
solo = g*p
group = g + p*t
print(1 if solo < group else 2 if solo > group else 0)