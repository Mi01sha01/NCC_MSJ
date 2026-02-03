t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if l == r == 1:
        print(1)
    else:
      print(r - l)