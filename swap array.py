# Swap array
def solve():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        
      n, k = map(int, input().strip().split())
      a = list(map(int, input().strip().split()))
      b = list(map(int, input().strip().split()))
    
      a = sorted(a)
      b = sorted(b)
    
      for i in range(k):
        if b[-(i+1)] > a[i]:
            a[i] = b[-(i+1)]
        else:
            break
      print(sum(a))            
    
        
solve()       
 
# 