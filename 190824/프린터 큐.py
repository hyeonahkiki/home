#백준- 큐문제 1966번

for tc in range(int(input())+1):
    n, m = map(int, input().split()) #n = 6, m= 0
    impo = list(map(int, input().split()))#[1, 1, 9, 1, 1, 1]
    idx = [t for t in range(1, n+1)] #[1, 2, 3, 4, 5, 6]
    order = idx[m] # idx[0] =1
    final = []

    while impo:
        if  impo[0] >= max(impo):
            num = impo.pop(0)
            idx_num=idx.pop(0)
            final.append(idx_num)
        else:
            num = impo.pop(0)
            impo.append(num)
            idx_num = idx.pop(0)
            idx.append(idx_num)
    print(final.index(order)+1)

