import sys

sys.stdin = open('input.txt', 'r')

# T = int(input())
# for tc in range(1, T + 1):
#     words = list(input())
#     H_cnt = int(input())
#     # 하이픈을 넣을 위치
#     position = list(map(int, input().split()))
#     position = sorted(position, reverse=True)
#     for i in position:
#         words.insert(i, '-')
#     print('#{} {}'.format(tc, ''.join(words)))

T = int(input())
for tc in range(1, T + 1):
    words = list(input())
    H_cnt = int(input())
    # 하이픈을 넣을 위치
    position = list(map(int, input().split()))
    position.sort()
    # 하이픈을 추가해서 문자의 길이가 늘어나는 만큼 인덱스를 옮겨 주기위해서
    move = 0
    for i in position:
        words.insert(i+move, '-')
        move += 1
    print('#{} {}'.format(tc, ''.join(words)))


# for tc in range(int(input())):
#     word, n= list(input()), int(input())
#     num = list(map(int, input().split()))
#     num.sort()
#     j=0
#     for i in range(n):
#         word.insert(num[i]+j, '-')
#         j+=1
#     print(f"#{tc+1} {''.join(word)}")

