n=int(input())
for I in range (n):
    x=list(map(int,input().split()))
    x.sort()
    b=len(set(x))
    if b==1 and x[0]%2==0:
        print("YES")
    elif x.count(min(x))==1 and b==2 and min(x)%2==0:
        print("YES") 
        
    elif x.count(max(x))==1  and b==2 and max(x)%2==0:
        print("YES")
        
    elif b==3 and ( x[2] -x[0])==x[1]:
        print('YES') 
    else:
        print('NO') 
            

