import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for x in range(N)]
    maxV = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                for s in range(M):
                    catch += flys[i+k][j+s]
            if catch > maxV:
                maxV = catch
    print('#{} {}'.format(tc, maxV))