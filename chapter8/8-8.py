'''
min을 쓰지 못했는데 그 이유가 나는 0이랑 비교했기 때문에.. 만약 min을 쓰려면 다른 값이랑 비교했어야 했음
index 에러가 있었는데, 최대 수로 맞추어줌..

2 15
2
3

3 4
3
5
7

'''
N,M=map(int,input().split())
coin=[]
x=[0]*(10000+1)#x=[0]*(M+1)
for i in range(N):
    coin.append(int(input()))
'''
coin[0] coin[1] coin[2]
   2       3       5
'''
coin.sort(reverse=True)
for j in range(len(coin)): #코인이 있는 곳은 x리스트를 1로 채우기
    x[coin[j]]=1

start=coin[-1]
'''
x[2] x[3] x[5]
 1    1    1
'''
for i in range(start+1,M+1): #코인이 있는 곳 다음부터
    for j in range(len(coin)):
        res= x[i - coin[j]] # 6-5 6-3
        if res!=0:
            x[i]=res+1
            break

if x[M]!=0:
    print(x[M])
else:
    print(-1)