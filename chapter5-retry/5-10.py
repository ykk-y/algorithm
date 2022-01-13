
N, M = map(int,input().split())
x=[]
for i in range(N):
    x.append(list(map(int,input())))

def dfs(i,j):
    if i<0 or i>=N or j<0 or j>=M: #종료조건을 쭉 적어보기.. =포함인지 확인 ..
        return False
    if x[i][j]==0:
        x[i][j]=1
        #그 다음이 뭐지?
        dfs(i-1,j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i , j+ 1)
        return True
    return False

cnt=0
#dfs 매개변수로 뭘넣어야하지 => 인덱스(좌표)생각
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            cnt+=1
print(cnt)