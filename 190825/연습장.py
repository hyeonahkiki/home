def maze(i, j, s):
    global n
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    # 초기화
    q = [] #큐생성
    s[i][j] = 1 #시작점 방문을 표시
    q.append([i,j]) #시작점 인큐

    while len(q) != 0: #큐가 비어있지 않으면 반복
        t = q.pop() #디큐
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if ni >=0 and ni <n and nj>=0 and nj< n: #미로를 벗어나지 않고
                if s[ni][nj] =='3':
                    return 1
                elif s[ni][nj] =='0': # 방문하지 않은 칸이면
                    s[ni][nj] = 1 #방문함을 표시
                    q.append([ni, nj]) #인큐하고
    return 0




for tc in range(1, int(input())+1):
    n = int(input())
    lists = [list(input()) for x in range(n)]
    startI = 0
    startJ= 0
    for i in range(n):
        for j in range(n):
            if lists[i][j] == '2':
                startI = i
                startj = j
    print('#{} {}'.format(tc, maze(startI, startJ, lists)))