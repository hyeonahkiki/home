import sys

sys.stdin = open('input.txt', 'r')


# 가로탐색해서 최소의 숫자를 더해나간다
# 탐색할 리스트, 최초의 합

T = int(input())
for tc in range(1, T + 1):
    # 배열판 크기
    N = int(input())
    boards = [list(map(int, input().split())) for x in range(N)]
    foot = []
    for i in range(N):
        for j in range(N):
           if not foot:
               foot.append([i,j])
    
        foot.append([i, j])
    print(foot)
    # print('#{} {}'.format(tc, cnt))