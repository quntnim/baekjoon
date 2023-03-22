s = input()
eng = [i for i in range(65,91)]
for i in eng:
    if chr(i) not in s:print(chr(i))
