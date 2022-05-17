s = input()
if 'A' in s:
    print(s.replace('B','A').replace('C','A').replace('D','A').replace('F','A'))
elif 'B' in s:
    print(s.replace('C','B').replace('D','B').replace('F','B'))
elif 'C' in s:
    print(s.replace('D','C').replace('F','C'))
else:
    for i in range(len(s)):
        print('A',end='')
    print()