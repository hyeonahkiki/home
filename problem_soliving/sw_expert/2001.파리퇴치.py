import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for x in range(N)]
    max_catch = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                for s in range(M):
                    catch += fly[i+k][j+s]
            if max_catch < catch:
                max_catch = catch
    print('#{} {}'.format(tc, max_catch))