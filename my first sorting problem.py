t=int(input())
for I in range (t):
    x,y=map(int,input().split())
    print(min(x,y),max(x,y))