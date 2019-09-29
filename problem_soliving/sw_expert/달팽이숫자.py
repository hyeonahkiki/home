import sys

sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    n = int(input())
    lists = [[0] * n for _ in range(n)]
    x, y = 0, 0
    # n값을 변형 시키지 않기 위해서
    a = n
    num = 1
    # n//2 해주는 이유는 4방향을 돌때가 1번 => 3일때는 1, 4일때는 2
    for i in range(n // 2):
        if n == 1:
            break
        for j in range(a - 1):
            lists[x][y + j] = str(num)
            num += 1
        # 다음 시작 위치 설정
        y = y + j + 1
        for r in range(a - 1):
            lists[x + r][y] = str(num)
            num += 1
        # 다음 시작 위치 설정
        x = x + r + 1
        for f in range(a - 1):
            lists[x][y - f] = str(num)
            num += 1
        # 다음 시작 위치 설정
        y = y - f - 1
        for d in range(a - 1):
            lists[x - d][y] = str(num)
            num += 1
        # 그 안에서 움직이는 값을 찾기 위해서
        a = a - 2
        # 시작 위치를 옮겨 주기 위해서
        x, y = x - d, y + 1
    if n % 2 == 1:
        lists[n // 2][n // 2] = str(n * n)
    print(f'#{tc + 1}')
    for fin in lists:
        print(' '.join(fin))
