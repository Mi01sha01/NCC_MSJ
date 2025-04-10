n=int(input())
m=[]
for I in range (n):
    x=list(input())
    m.append(x)

def n_d_e(matrix):
    n = len(matrix)
    result = []
    for i in range(n):
        for j in range(n):
            if i != j and i + j != n - 1:
                result.append(matrix[i][j])
    return result
    

def p_d(m):
    return[m[i][i] for i in range(len(m))]   
 
def s_d(m):
    n=len(m)
    return[m[i][n-1-i] for i in range(n)]   
a=p_d(m)    
b=s_d(m)
c=n_d_e(m)
d=set(c)
e=len(d)
f=set(a)
l=len(f)

if a==b and c!=b and c[0] != b[0] and e==1 and l==1:
    print("YES")
else:
    print("NO")    
    