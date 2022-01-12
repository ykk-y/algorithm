"""
입력을 하나로 끊어서 ?=> map(int,input()) 00110 -> [0,0,1,1,0]
다음을 어떻게 확인하지? 이어진 곳.. 그리고 아랫줄?=> index x,y를 이용하기!
00110
00011
11111
00000


15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

"""
N,M= map(int,input().split())
graph=[]
cnt=0
for i in range(N):
    graph.append(list(map(int,input())))
def dfs(x,y):
    #만약 방문했다면 False? 아님 벗어난 경우를 들어야 함
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if graph[x][y] == 0:
        graph[x][y]=1
        #방문 안했다면 #위치는 상하좌우임.. 그리고 +1, +1 안됨
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            cnt+=1
print(cnt)



