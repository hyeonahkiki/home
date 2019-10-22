import sys
sys.stdin = open('input.txt', 'r')

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    min_S= 100000000
    max_S = 0


    for i in range(0, N-M+1):
        part_s = 0
        for k in range(M):
            part_s += nums[i+k]
        if part_s > max_S:
            max_S = part_s
        if part_s < min_S:
            min_S = part_s
    print('#{} {}'.format(tc, max_S-min_S))