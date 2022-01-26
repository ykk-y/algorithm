'''
5
8 3 7 9 2
3
5 7 9
'''
'''
5
2 3 7 8 9
3
5 7 9
'''


N=int(input())
x=list(map(int,input().split())) # list(map()) list!!
M=int(input())
y=list(map(int,input().split()))
x.sort()
y.sort()

def bs(target,start,end):
    #어디랑 target 비교하는거지?
    #만약 mid가 start end 같다면 종료를 어디서..!?
    mid = (start+end)//2
    ret=0
    if target == x[mid]:
        return True
    elif target < x[mid]:
        if start == end:
            return False
        ret=bs(target,start,mid-1)
    elif target > x[mid]:
        if start == end:
            return False
        ret=bs(target,mid+1,end)
    return ret

def solution_1():
    for data in y:
        result=bs(data,0,N-1)
        if result :
            print('yes',end=' ')
        else:
            print('no',end=' ')
solution_1()

