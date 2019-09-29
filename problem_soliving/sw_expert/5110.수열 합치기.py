import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #수열의 길이, 수열의 개수
    standard = list(map(int, input().split())) # 기준이 되는 수열
    for x in range(M-1): #기준이 되는 수열을 하나 빼고
        num_seq = list(map(int, input().split()))
        first_num = num_seq[0]
        for i in range(N):
            if standard[i] > first_num:
                standard = standard[:i] + num_seq +standard[i:]
                break
        else:
            standard = standard + num_seq
    if len(standard) >=10:
        standard = standard[::-1]
    standard = list(map(str, standard))

    print('#{} {}'.format(tc, ' '.join(standard[:10])))

