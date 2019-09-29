scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for tc in range(1, T+1):
    res = []
    students, num = map(int, input().split())
    for i in range(students):
        middle, final, hw = map(int, input().split())
        total_s = (middle * 0.35) + (final * 0.45) + (hw * 0.2)
        res.append(total_s)
    sort_res = sorted(res, reverse=True)
    target = sort_res.index(res[num-1]) # res[num-1]의 위치를 반환해준다.
    cnt = students // 10

    print('#{} {}'.format(tc, scores[target//cnt]))
