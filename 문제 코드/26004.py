input()
s = input()
arr = []
for i in "HIARC":
    arr.append(s.count(i))
print(min(arr))