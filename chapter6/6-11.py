'''
x.append()에서 2개 argument가 들어갈 때는 ( str , int ) 해서
x.append( (str , int) ) 이렇게 넣어주기
#람다??? lambda 매개변수 : return =>매개변수는 global인 경우는 따로 안받나?
2
홍길동 95
이순신 77
'''
N=int(input())
x=[]
min=101
for i in range(N):
    tmp = input().split()
    x.append((tmp[0], int(tmp[1])))
j_index=-1
for i in range(N):
    for j in range(i,N):
        if x[j][1]<min:
            j_index=j
    if j_index != -1:
        x[i],x[j_index]=x[j_index], x[i]
for i in range(N):
    print(x[i][0],end=' ')

