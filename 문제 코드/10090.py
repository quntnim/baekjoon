import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().rstrip().split()))
cnt = 0
def merge_sort(arr):
    global cnt,n

    if n <= 1:
        return

    mid = n // 2
    left_group = arr[:mid]  
    right_group = arr[mid:]

    merge_sort(left_group)
    merge_sort(right_group)

    left = 0
    right = 0
    now = 0

    swap = 0
    
    while left < mid and right < n:
        if left_group[left] < right_group[right]:
            arr[now] = left_group[left]
            left += 1
            now += 1
            cnt+=swap

        else:
            arr[now] = right_group[right]
            right += 1
            now += 1
            swap+=1

    while left < len(left_group):
        arr[now] = left_group[left]
        left += 1
        now += 1
        cnt += swap

merge_sort(arr)
print(cnt)