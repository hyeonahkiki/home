while i < N:
    i += 1
    cnt += 1
    if carrot[i] >= M:
        carrot[i] -= M
        cnt += i
        i = 0
    else:
        if i != N:
            carrot[i + 1] += carrot[i]
            carrot[i] = 0
        else:
            cnt += N
print(cnt)
