n=int(input())
count=0
for I in range(n):
    s=input()
    if "++"in s:
        count+=1
    elif "--" in s:
        count-=1
print(count)
