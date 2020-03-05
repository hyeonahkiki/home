import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))
    # 무조건 0점은 들어가기 때문에 1체크
    check = [1] + [0] *(sum(score))
    cnt = 1
    for i in range(N):
        for j in range(len(check)-1, -1, -1):
            if check[j] ==1:
                if check[j+score[i]] ==0:
                    cnt +=1
                    check[j+score[i]] = 1
    print('#{} {}'.format(tc, cnt))

