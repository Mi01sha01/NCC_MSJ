n=int(input())
m=[]
for I in range (n):
    x=list(map(int,input().split()))
    m.append(x)
x=len(m)    
def p_d(m):
    return[m[i][i] for i in range(len(m))]
def s_d(m):
    return[m[i][x-1-i] for i in range(x)]
def m_r(m):
    return[m[n//2][i] for i in range(x)]
def m_c(m):
    return[m[i][n//2] for i in range(x)]    
a=p_d(m) 
b=s_d(m)
b.remove(b[(len(b)-1)//2])  
c=m_r(m)
c.remove(c[(len(c)-1)//2])
d=m_c(m)
d.remove(d[(len(d)-1)//2])
print(sum(a)+sum(b)+sum(c)+sum(d))
