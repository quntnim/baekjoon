from collections import Counter
arr = list(map(int,input().split()))
cnt = Counter(arr)
print(cnt.most_common(1)[0][0])