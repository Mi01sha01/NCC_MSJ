n=int(input())
a=set(map(int, input().split()))
b=int(input())
b=set(map(int, input().split()))

print(len(a.difference(b)))