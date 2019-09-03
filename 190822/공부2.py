import sys
sys.stdin = open('input1.txt', 'r')

for tc in range(int(input())+1):
    N = int(input())
    numbers = [list(input().split()) for x in range(N)]

    for i in range(N):
        for j in range(N):
            ans_90 = []
            ans_180= []
            ans_270= []
            for k in range(N):
                ans_90.append(numbers[i+k][j+N-1])
                ans_90.append(numbers[i+N-1][j+N-1-k])
                ans_90.append(numbers[i-k][j])
            for m in range(N):
                ans_180.append(numbers[i+N-1][j+N-1])
                ans_180.append(numbers[i+N//2][j+N//2])
                ans_180.append(numbers[i+m][j+m])
            for s in range(N):
                ans_270.append(numbers[i+N-1-s][j+N-1])
                ans_270.append(numbers[i][j+N-1-s])
                ans_270.append(numbers[i+1][j])

        print('#{}'.format(tc))
        print()
        print(' '.join(ans_90))
        print(' '.join(ans_180))
        print(' '.join(ans_270))