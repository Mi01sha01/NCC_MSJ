a = int(input())
b = int(input())
c = int(input())
 
result = max(a + b + c, a * b * c, (a + b) * c, a * (b + c))
print(result)