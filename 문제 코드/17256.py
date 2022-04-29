ax, ay, az = map(int,input().split())
cx, cy, cz = map(int,input().split())
print(cx - az, cy // ay, -(ax - cz))