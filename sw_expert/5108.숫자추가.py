T = int(input())
for tc in range(1, T+1):
    N, M, L= map(int, input().split()) #수열의 길이, 추가횟수, 출력할 인덱스
    numbers = list(map(int, input().split()))
    for x in range(M):
        order, add_num = map(int, input().split())
        numbers.insert(order, add_num)
    print('#{} {}'.format(tc, numbers[L]))
