import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    nums = [list(map(int, input().split())) for x in range(n)]
    row_idx = 0 #가로 탐색위치
    row_cnt = 0
    col_idx = 0
    col_cnt = 0

    for j in range(n):
        while row_idx < n:
            while row_idx <n and nums[row_idx][j] ==0:
                  row_idx += 1
            r_cnt = 0
            while row_idx < n and nums[row_idx][j] ==1:
                 r_cnt += 1
                 row_idx +=1
        if r_cnt == k:
            row_cnt += 1

    for i in range(n):
        while col_idx < n:
            while col_idx <n and nums[i][col_idx]==0:
                col_idx += 1
            c_cnt = 0
            while col_idx < n and nums[i][col_idx]==1:
                c_cnt +=1
                col_idx +=1
        if c_cnt == k:
            col_cnt +=1
    finish = row_cnt + col_cnt
    print('#{} {}'.format(tc, finish))