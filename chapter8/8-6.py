N=int(input())
x=list(map(int,input().split()))
tot=len(x)
a=[0]*(tot)
a[0]=x[0]
a[1]=max(x[0],x[1])
for i in range(0,tot-2):
    a[i+2]=max(a[i]+x[i+2],a[i+1])

print(a[N-1])
'''
1 3 1 5

1 3 2/[3] 3+5/3
          

N읙 갯수=>여기서는 3부터 시작한다는 점, 짝지어지는 것이 있는지 보기
=> DP는 사실상 이전의 전은 관심이 없는게 아닐까? 전까지만 관심이 있고..(점화식)
'''