import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_kill = 0
            for k in range(M):
                for s in range(M):
                    fly_kill += nums[i+k][j+s]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

    # ㄱ 모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                fly_kill += nums[i][j+k]
                fly_kill += nums[i+k][j+M-1]
            fly_kill -= nums[i+k][j+M-1]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

#ㄷ 모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                fly_kill += nums[i][j+k]
                fly_kill += nums[i+k][j]
                fly_kill += nums[i+M-1][j+k]
            fly_kill -= nums[i][j]
            fly_kill -= nums[i+M-1][j]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

#ㄴ모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                fly_kill += nums[i+k][j]
                fly_kill += nums[i + M - 1][j + k]
            fly_kill -= nums[i + M - 1][j]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

# ㅁ 모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                fly_kill += nums[i+k][j]
                fly_kill += nums[i + M - 1][j + k]
                fly_kill += nums[i+k][j+M-1]
                fly_kill += nums[i][j+k]
            fly_kill -= nums[i + M - 1][j]
            fly_kill -= nums[i][j]
            fly_kill -= nums[i+M-1][j+M-1]
            fly_kill -= nums[i][j+M-1]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

# x자 모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                fly_kill += nums[i+k][j+k]
                fly_kill += nums[i+k][j+M-1-k]
            if M %2:
                fly_kill -= nums[i+M//2][j+M//2]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))

# 모자이크 모양
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(N)]
    max_kill = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_kill = 0
            for k in range(M):
                if k % 2:
                    for r in range(M):
                        if r % 2 ==0:
                            fly_kill += nums[i+k][j+r]
                else:
                    for c in range(M):
                        if c % 2:
                            fly_kill += nums[i+k][j+c]
            if max_kill < fly_kill:
                max_kill = fly_kill

    print('#{} {}'.format(tc, max_kill))
