# Dutch National Flag Algorithm 
col=list(map(int,input().split()))
def sor_col(col):
    # l is boundary for 0s,m is current element and h is boundary for 2s.
    l,m,h=0,0,len(col)-1
    while m<=h:
        if col[m]==0:
            col[l],col[m]=col[m],col[l]
            l+=1
            m+=1
        elif col[m]==1:
            m+=1
        else:
            # when col[m]==2
            col[m],col[h]=col[h],col[m]
            h-=1
            
sor_col(col)
print(col)
                
    