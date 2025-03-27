n,m,k=map(int,input().split())
board=[['.' for I in range(m)] for I in range(n)]
for I in range(k):
    y,x=map(int,input().split())
    board[y-1][x-1]="*"
for I in board:
    print(''.join(I))   