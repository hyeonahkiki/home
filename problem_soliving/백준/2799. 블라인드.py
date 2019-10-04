import sys
sys.stdin = open('input', 'r')

# 한층의 창문 개수, 층수
M, N = map(int, input().split())
window = [list(input()) for x in range(5*M+1)]
check = [0] * 5

for i in range(1, 5*M+1, 5):
    for j in range(1, 5*N+1, 5):
        cnt= 0
        for k in range(4):
            if window[i+k][j:j+4][0]=='*':
                cnt +=1
        check[cnt] += 1
check = list(map(str, check))
print(' '.join(check))