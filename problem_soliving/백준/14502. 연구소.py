import sys
sys.stdin = open('input', 'r')




di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 0좌표를 다 뽑기
# 여기서 랜덤으로 3개씩 뽑기
# 뽑은 좌표를 1로 만들기
# 바이러스 퍼뜨리기
# 0을 카운트하기
# 다시 뽑은 좌표들(1로된거)을 0으로 만들기





# 가로, 세로
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for x in range(N)]
visited = [[0]* M for x in range(N)]

# 0의 좌표값을 다 담아서 가기
zero = []
maxV = 0
for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            visited[i][j] =2
        elif lab[i][j] == 1:
            visited[i][j] = 1
        else:
            zero.append([i, j])

# 0좌표를 세개씩 뽑기
for a in range(0, len(zero)-2):
    for b in range(a+1, len(zero)-1):
        for c in range(b+1, len(zero)):
            pass
