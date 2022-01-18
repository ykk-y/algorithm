N=int(input())
x=[]

for i in range(N):
    x.append(input().split())
x.sort(key=lambda s: (-int(s[1]),int(s[2]),-int(s[3]),(s[0])))

for i in range(N):
    print(x[i][0])