a = []
for i in range(4):
    a.append(int(input()))
if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:print("Fish At Constant Depth")
elif a[0] > a[1] and a[1] > a[2] and a[2] > a[3]:print("Fish Diving")
elif a[0] < a[1] and a[1] < a[2] and a[2] < a[3]:print("Fish Rising")
else:print("No Fish")