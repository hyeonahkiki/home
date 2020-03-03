import sys

sys.stdin = open('input', 'r')

# # 구역나누면서 바로 탐색하기
# def division(n, k, s, z):
#     global visited
#     if n == k:
#         groupB = []
#         for part in list(range(1, N + 1)):
#             if part not in s:
#                 groupB.append(part)
#         visited = [0] * (N + 1)
#         ansA = bfs(s)
#         ansB = bfs(groupB)
#         # print(groupA, groupB)
#         # print(ansA, ansB)
#         if ansA == True and ansB == True:
#             print(len(s))
#             print(' '.join(map(str, s)))
#             print(len(groupB))
#             print(' '.join(map(str, groupB)))
#             return 1
#     else:
#         for i in range(z, N + 1):
#             if used[i] != 1:
#                 used[i] = 1
#                 # 결과값을 하나만 출력하고 끝내기 위한 조건
#                 if division(n + 1, k, s + [i], i) == 1:
#                     return 1
#                 used[i] = 0
#     return
#
#
# def bfs(lists):
#     global visited
#     if len(lists) == 1:
#         return True
#     else:
#         q = [lists[0]]
#         while q:
#             human = q.pop(0)
#             visited[human] = 1
#             for part in lists:
#                 if check[human][part] == 1:
#                     return False
#                 if check[human][part] ==0 and visited[part] ==0:
#                     q.append(part)
#                     visited[part] = 1
#         return True
#
#
# N = int(input())
# info = [list(map(int, input().split())) for x in range(N)]
#
# # 싫어하는 사람 표시하기
# check = [[0] * (N + 1) for x in range(N + 1)]
# for i in range(N):
#     spot = info[i]
#     for x in range(1, len(spot)):
#         check[i + 1][spot[x]] = 1
#
# # 팀나누기
# for i in range(1, N):
#     used = [0] * (N + 1)
#     # 재귀에서 나오기 위한 조건을 입력
#     if division(0, i, [], 1) == 1:
#         break

N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
team_check = [2] * N
q = []
for stu in range(N):
    if team_check[stu] == 2:
        team_check[stu] = 0
        for enemy in students[stu][1:]:
            if team_check[enemy-1] == 2:
                team_check[enemy-1] = 1
                q.append(enemy-1)
        while len(q) != 0:
            my_idx = q.pop(0)
            my_num = team_check[my_idx]
            for my_enemy in students[my_idx][1:]:
                if team_check[my_enemy-1] == 2:
                    team_check[my_enemy-1] = (my_num + 1) % 2
                    q.append(my_enemy-1)

team_blue = []
team_white = []
for idx in range(N):
    if team_check[idx] == 0:
        team_blue.append(idx+1)
    else:
        team_white.append(idx+1)

team_blue_cnt = len(team_blue)
team_white_cnt = len(team_white)
print(team_blue_cnt)
for team_blue_member in team_blue:
    print(team_blue_member, end=' ')
print()
print(team_white_cnt)
for team_white_member in team_white:
    print(team_white_member, end=' ')