n=int(input())
for I in range (n):
  y=[]
  for I in range (4):
    x=list(map(int,input().split()))
    y.append(x)
  if y[0][0] !=y[1][0]:
    print((y[0][0]-y[1][0])**2) 
  elif y[0][0]==y[1][0]:
    print((y[0][0]-y[2][0])**2)
    