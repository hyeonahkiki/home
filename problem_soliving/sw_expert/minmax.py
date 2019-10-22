import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    maxV = 0
    minV = 10000000
    for i in range(N):
        if nums[i] > maxV:
            maxV = nums[i]
        if nums[i] < minV:
            minV = nums[i]

    print('#{} {}'.format(tc, maxV-minV))