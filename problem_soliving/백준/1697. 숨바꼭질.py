import sys

sys.stdin = open('input', 'r')

f = [-1, 1, 2]

def bfs(n, k):
    visited = [0] * 100001
    q = [n]
    visited[n] = 1
    while q:
        x = q.pop(0)
        for i in range(3):
            if i == 2:
                ni = x * f[i]
            else:
                ni = x + f[i]
            if 0 <= ni < 100001 and visited[ni] == 0:
                visited[ni] = visited[x] + 1
                q.append(ni)
    return visited


# 언니, 동생위치
N, K = map(int, input().split())
print(bfs(N, K)[K] - 1)
