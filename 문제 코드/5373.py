t = int(input())

def rotate_90(arr: list):
    rotate_arr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for l in range(3):
            rotate_arr[l][2-i]=arr[i][l]
    return rotate_arr

def reverse_rotate_90(arr: list):
    rotate_arr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for l in range(3):
            rotate_arr[2-l][i]=arr[i][l]
    return rotate_arr

for _ in range(t):
    up = [
        ['w','w','w'],
        ['w','w','w'],
        ['w','w','w']
    ]
    down = [
        ['y','y','y'],
        ['y','y','y'],
        ['y','y','y']
    ]
    front = [
        ['r','r','r'],
        ['r','r','r'],
        ['r','r','r']
    ]
    back = [
        ['o','o','o'],
        ['o','o','o'],
        ['o','o','o']
    ]
    left = [
        ['g','g','g'],
        ['g','g','g'],
        ['g','g','g']
    ]
    right = [
        ['b','b','b'],
        ['b','b','b'],
        ['b','b','b']
    ]

    n = int(input())
    com = list(input().split())
    for cm in com:
        tmp = 0
        a=''
        b=''
        c=''
        side = cm[0]
        spin = cm[1]

        if side == 'U':
            if spin =='+':
                up = rotate_90(up)
                tmp = front[0]
                front[0] = right[0]
                right[0] = [back[2][2],back[2][1],back[2][0]]
                back[2][2],back[2][1],back[2][0] = left[0]
                left[0] = tmp
            if spin =='-':
                up = reverse_rotate_90(up)
                for i in range(3):
                    tmp = front[0]
                    front[0] = right[0]
                    right[0] = [back[2][2],back[2][1],back[2][0]]
                    back[2][2],back[2][1],back[2][0] = left[0]
                    left[0] = tmp

        if side == 'D':
            if spin =='+':
                down = rotate_90(down)
                tmp = front[2]
                front[2] = left[2]
                left[2] = [back[0][2],back[0][1],back[0][0]]
                back[0][2],back[0][1],back[0][0] = right[2]
                right[2] = tmp
            if spin =='-':
                down = reverse_rotate_90(down)
                for i in range(3):
                    tmp = front[2]
                    front[2] = left[2]
                    left[2] = [back[0][2],back[0][1],back[0][0]]
                    back[0][2],back[0][1],back[0][0] = right[2]
                    right[2] = tmp

        if side == 'F':
            if spin =='+':
                front = rotate_90(front)
                a,b,c = up[2][0],up[2][1],up[2][2]
                up[2] = [left[2][2],left[1][2],left[0][2]]
                left[2][2],left[1][2],left[0][2] = down[0][2],down[0][1],down[0][0]
                down[0][2],down[0][1],down[0][0] = right[0][0],right[1][0],right[2][0]
                right[0][0],right[1][0],right[2][0] = a,b,c
            if spin =='-':
                front = reverse_rotate_90(front)
                for i in range(3):
                    a,b,c = up[2][0],up[2][1],up[2][2]
                    up[2] = [left[2][2],left[1][2],left[0][2]]
                    left[2][2],left[1][2],left[0][2] = down[0][2],down[0][1],down[0][0]
                    down[0][2],down[0][1],down[0][0] = right[0][0],right[1][0],right[2][0]
                    right[0][0],right[1][0],right[2][0] = a,b,c

        if side == 'B':
            if spin =='+':
                back = rotate_90(back)
                a,b,c = up[0][0],up[0][1],up[0][2]
                up[0] = [right[0][2],right[1][2],right[2][2]]
                right[0][2],right[1][2],right[2][2] = down[2][2],down[2][1],down[2][0]
                down[2][2],down[2][1],down[2][0] = left[2][0],left[1][0],left[0][0]
                left[2][0],left[1][0],left[0][0] = a,b,c
            if spin =='-':
                back = reverse_rotate_90(back)
                for i in range(3):
                    a,b,c = up[0][0],up[0][1],up[0][2]
                    up[0] = [right[0][2],right[1][2],right[2][2]]
                    right[0][2],right[1][2],right[2][2] = down[2][2],down[2][1],down[2][0]
                    down[2][2],down[2][1],down[2][0] = left[2][0],left[1][0],left[0][0]
                    left[2][0],left[1][0],left[0][0] = a,b,c

        if side == 'L':
            if spin =='+':
                left = rotate_90(left)
                a,b,c = up[0][0],up[1][0],up[2][0]
                up[0][0],up[1][0],up[2][0] = back[0][0],back[1][0],back[2][0]
                back[0][0],back[1][0],back[2][0] = down[0][0],down[1][0],down[2][0]
                down[0][0],down[1][0],down[2][0] = front[0][0],front[1][0],front[2][0]
                front[0][0],front[1][0],front[2][0] = a,b,c
            if spin =='-':
                left = reverse_rotate_90(left)
                for i in range(3):
                    a,b,c = up[0][0],up[1][0],up[2][0]
                    up[0][0],up[1][0],up[2][0] = back[0][0],back[1][0],back[2][0]
                    back[0][0],back[1][0],back[2][0] = down[0][0],down[1][0],down[2][0]
                    down[0][0],down[1][0],down[2][0] = front[0][0],front[1][0],front[2][0]
                    front[0][0],front[1][0],front[2][0] = a,b,c

        if side == 'R':
            if spin =='+':
                right = rotate_90(right)
                a,b,c = up[0][2],up[1][2],up[2][2]
                up[0][2],up[1][2],up[2][2] = front[0][2],front[1][2],front[2][2]
                front[0][2],front[1][2],front[2][2] = down[0][2],down[1][2],down[2][2]
                down[0][2],down[1][2],down[2][2] = back[0][2],back[1][2],back[2][2]
                back[0][2],back[1][2],back[2][2] = a,b,c
            if spin =='-':
                right = reverse_rotate_90(right)
                for i in range(3):
                    a,b,c = up[0][2],up[1][2],up[2][2]
                    up[0][2],up[1][2],up[2][2] = front[0][2],front[1][2],front[2][2]
                    front[0][2],front[1][2],front[2][2] = down[0][2],down[1][2],down[2][2]
                    down[0][2],down[1][2],down[2][2] = back[0][2],back[1][2],back[2][2]
                    back[0][2],back[1][2],back[2][2] = a,b,c
                    
    print(''.join(up[0]))
    print(''.join(up[1]))
    print(''.join(up[2]))