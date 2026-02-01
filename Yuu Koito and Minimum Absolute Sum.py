t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = a[:]

    
    if a[0] != -1 and a[-1] != -1:
        ans = abs(a[-1] - a[0])
    
    elif a[0] != -1 and a[-1] == -1:
        res[-1] = a[0]
        ans = 0

    elif a[0] == -1 and a[-1] != -1:
        res[0] = a[-1]
        ans = 0

    
    else:
        res[0] = 0
        res[-1] = 0
        ans = 0

    
    for i in range(n):
        if res[i] == -1:
            res[i] = 0

    print(ans)
    print(*res)