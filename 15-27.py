'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''
N, x=map(int,input().split())
y=list(map(int,input().split()))

# k=[0]*2000000001 계수정렬은 안됨.. 음수 ..


#   11255557899 이때 5를 찾는다면, 랜담위치에서 5를 찾고 거길 기준으로 앞으로 가고 뒤로도 가는 방법
# return -1이 None Type..
def solution_1():
    y.sort()
    find=binary(x,0,N-1)
    if find == None:
        print(-1)
        return False
    tmp=find
    cnt=0
    print(tmp)
    while x==y[tmp]:
        if y[tmp]==x:
            cnt+=1
            tmp-=1
        else :
            break
    tmp=find+1
    while x==y[tmp]:
        if y[tmp]==x:
            cnt+=1
            tmp+=1
        else :
            break
    print(cnt)

def binary(target,start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if target==y[mid]:
        return mid
    elif target<y[mid]:
        binary(target,start,mid-1)
    else :
        binary(target,mid+1,end)

solution_1()