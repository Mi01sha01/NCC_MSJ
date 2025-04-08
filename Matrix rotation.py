def rotate(x):
    x[0][0],x[0][1],x[1][0],x[1][1]=x[1][0],x[0][0],x[1][1],x[0][1]
    return x
n=int(input())
for I in range (n):
  y=[]
  for j in range(2):
    x=list(list(map(int,input(). split())))
    y.append(x)
  b=y[0][0]<y[0][1]  and y[0][0]<y[1][0] and y[0][1]<y[1][1] and y[1][0]<y[1][1]
  if b==1:
      print("YES")
      
  elif b==0:
      for I in range(4):
          y=rotate(y)
          b=y[0][0]<y[0][1]  and y[0][0]<y[1][0] and y[0][1]<y[1][1] and y[1][0]<y[1][1]
          if b==1:
              m="yes"
              
              break 
          else:    
              m="NO"
      
      print(m)
      
 