n=int(input())
for I in range(n):
    com =input()
    if com[0:10]=="Simon says":
        print(com[10:])