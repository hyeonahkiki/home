import sys
sys.stdin = open('input', 'r')

# 8방향 돌아줄것을 정리(근데 이동하는 중간에 있어도 잡을 수없기에)
# 튜플로 3개를 세트로 묶어줘야한다
di = [(-1,-2, -3), (-1, -2, -3), (0, -1, -2), (0, 1, 2), (1, 2, 3), (1, 2, 3), (0, 1, 2), (0, -1, -2)]
dj = [(0, -1, -2), (0, 1, 2), (1, 2, 3), (1, 2, 3), (0, 1, 2), (0, -1, -2), (-1, -2, -3), (-1, -2, -3)]

# 마지막 지점에서 왕이 있는지를 확인 . 그전에 왕이 있으면
# break 걸기

def check(x, y):
    global visited, r2, c2
    q = [0] * 10 * 9
    front=rear= -1
    rear += 1
    q[rear] = [x, y]
    visited[x][y] = 1
    while front != rear:
        front += 1
        i,j = q[front]
        for k in range(8):
            for s in range(3):
                ni = i + di[k][s]
                nj = j + dj[k][s]
                if 0<=ni<10 and 0<=nj < 9 and visited[ni][nj] == 0:
                    # 중간에 왕을 만났을 때 바로 끝
                    if ni ==r2 and nj==c2 and s <2:
                        break
                    # 끝점에서 왕을 만날때
                    elif ni == r2 and nj == c2 and s==2:
                        return visited[i][j]
                    # 끝점인데 아무점도 아닐때
                    # and로 묶어버리면 같은행 같은 열에 있는 점에 아예 q에 넣을 수가 없음
                    elif (ni != r2 or nj != c2) and s==2:
                        visited[ni][nj] = visited[i][j] + 1
                        rear += 1
                        q[rear] = [ni,nj]



# 상의 위치
r1, c1 = map(int, input().split())
# 왕의 위치
r2, c2 = map(int, input().split())
# 장기판 생성
visited = [[0] * 9 for x in range(10)]
# 몇번만에 왕에 도달하는지
print(check(r1, c1))