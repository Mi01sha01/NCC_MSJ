t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = []
    i = 0
    while i < n:
        a.append(s[i])
        j = i + 1
        while j < n and s[j] != s[i]:
            j += 1
        i = j + 1
    print(''.join(a))