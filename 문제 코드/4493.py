import sys
input = sys.stdin.readline

for i in range(int(input())):
    asc=0;bsc=0
    for i in range(int(input())):
        a,b = input().split()
        if a == b:continue
        elif a == 'R':
            if b == 'P':bsc+=1
            if b == 'S':asc+=1
        elif a == 'P':
            if b == 'S':bsc+=1
            if b == 'R':asc+=1
        elif a == 'S':
            if b == 'R':bsc+=1
            if b == 'P':asc+=1
    if asc == bsc:print('TIE')
    else:print('Player 1'if asc > bsc else'Player 2')