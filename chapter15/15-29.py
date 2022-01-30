N,C=map(int,input().split())
x=[]
for i in range(N):
    x.append(int(input()))

x.sort()

def b_s(start,end,target):
    if start>end:
        return None
    mid=(start+end)//2
    while i in range(mid):
        if x[end]-x[mid] > x[mid]- x[start]:
            #return b_s(start,end,target)
        elif x[end] -x[mid] < x[mid] - x[start]:
            #return b_s(mid+1,end,target)
        else:
            #return mid

'''

def b_s(start,end,target):
    if start>end:
        return None
    mid=(start+end)//2
    if x[mid] > target:
        return b_s(start,mid-1,target)
    elif x[mid] < target:
        return b_s(mid+1,end,target)
    else:
        return mid

'''