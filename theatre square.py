import math
n, m, a = map(int, input().split())
 
 
flagstones_along_length = math.ceil(n / a)
flagstones_along_width = math.ceil(m / a)
 
 
total_flagstones = flagstones_along_length * flagstones_along_width
 
# Output the result
print(total_flagstones