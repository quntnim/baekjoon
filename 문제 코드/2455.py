peak = []
now = 0
for i in range(4):
    a,b = map(int,input().split())
    now = now+b-a
    peak.append(now)
print(max(peak))