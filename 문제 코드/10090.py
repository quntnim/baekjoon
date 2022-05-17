import sys
input = sys.stdin.readline
input()
arr = list(map(int,input().rstrip().split()))
cnt = 0
def merge_sort(num):
    global cnt
    m = len(num)

    if m <= 1:
        return
    if num == sorted(num):
        return

    mid = m // 2
    left_group = num[:mid]
    right_group = num[mid:]

    merge_sort(left_group)
    merge_sort(right_group)

    left = 0
    right = 0
    now = 0

    swap = 0
    
    while left < len(left_group) and right < len(right_group):
        if left_group[left] < right_group[right]:
            num[now] = left_group[left]
            left += 1
            now += 1
            cnt+=swap

        else:
            num[now] = right_group[right]
            right += 1
            now += 1
            swap+=1

    while left < len(left_group):
        num[now] = left_group[left]
        left += 1
        now += 1
        cnt += swap

    while right < len(right_group):
        num[now] = right_group[right]
        right += 1
        now += 1

merge_sort(arr)
sys.stdout.write(str(cnt))