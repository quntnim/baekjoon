arr = list(map(int,input().split()))
team1 = arr[0] + arr[3]
team2 = arr[2] + arr[1]
print(abs(team1 - team2))