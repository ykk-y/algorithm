import sys
from math import floor
import copy
N,M,K=map(int,sys.stdin.readline().split())
graph=[[(0,0,0,0)]*N for _ in range(N)]
after=[[(0,0,0,0)]*N for _ in range(N)]
dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for i in range(M):
    r,c,m,s,d=map(int,sys.stdin.readline().split())
    graph[r-1][c-1]=(m,s,d,1)
def move(i,j,m,s,d):
    ds = s % N  # 이동량
    x, y = (i+ (dir[d][0] * ds))%N, (j+(dir[d][1] * ds))%N
    if after[x][y][0] == 0: #처음 입력
        after[x][y] = (m, s, d,1)
    else: # 이미 입력되어 있는 경우
        tmpm, tmps, tmpd,tmpc = after[x][y]
        m += tmpm
        s += tmps
        if d==-1:
            after[x][y]=(m,s,d,tmpc+1)
        else:
            if d % 2 == tmpd % 2:  # 표현? 모두 짝수거나 모두 홀수..
                after[x][y]=(m,s,d,tmpc+1)
            else:
                after[x][y]=(m,s,-1,tmpc+1)
for _ in range(K):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0]!=0:
                m,s,d,cnt=graph[i][j]#질량 속력 방향, 갯수
                if cnt==1:
                    move(i,j,m,s,d)
                else:
                    if d==-1 :
                        tmp=1
                    else:
                        tmp=0
                    nm=floor(m/5)
                    if nm==0:
                        continue
                    ns=floor(s/cnt)
                    for direction in range(tmp,8,2):
                        move(i,j,nm,ns,direction)
    graph=copy.deepcopy(after)
    after = [[(0, 0, 0, 0)] * N for _ in range(N)]
sum=0
for i in range(N):
    for j in range(N):
        m,_,_,c =graph[i][j]
        if c!=1:
            m=floor(m/5)*4
        sum+=m
print(sum)
