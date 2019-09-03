# 백준 - 큐문제

n, k = map(int, input().split())
que = [t for t in range(1, n+1)]
ans = []

i = 1
while que:
        if i % k == 0:
            pick = que.pop(0)
            ans.append(pick)
            i += 1
        else:
            pick = que.pop(0)
            que.append(pick)
            i += 1
res = list(map(str, ans))

print('<' + ', '.join(res) + '>')




