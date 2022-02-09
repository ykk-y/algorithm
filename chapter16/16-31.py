'''
3 4
1 3 3 2 2 1 4 1 0 6 4 7

4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
#T=int(input())
n,m=map(int,input().split())
x=[]
tmp=list(map(int,input().split()))
index=0
for i in range(n):
    x.append(tmp[index:index+m])
    index+=m
y=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
        y[i][0]=x[i][0]
dir=[(-1,1),(0,1),(1,1)]
for j in range(0,m-1):#열
    for i in range(n):#행
        for k in range(3):
            x_,y_=dir[k][0]+i,dir[k][1]+j
            if x_>=0 and x_<n and y_>=0 and y_<m:
                y[x_][y_] = max(y[i][j] + x[x_][y_], y[x_][y_])

tmp=0
for i in range(n):
    tmp=max(tmp,y[i][m-1])
print(tmp)