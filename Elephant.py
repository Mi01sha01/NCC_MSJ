x=int(input())
y=range(1,6)
z=0
while True:
    
  if x in y:
     z+=1
     break
  else:
      x=x-5
      z+=1
print(z)         

     