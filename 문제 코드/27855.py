a,b=map(int,input().split())
first = a*3 + b
c,d=map(int,input().split())
second = c*3 + d
print("NO SCORE"if first == second else f'1 {first-second}' if first > second else f'2 {second-first}')