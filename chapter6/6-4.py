'''
어 헷갈린다.
내가 생각한건 left는 작은거면 그대로? 두고 넘어가는걸로 생각했는데
무조건 right는 작은걸 택해야하고 left는 큰걸 택해야 함. 그러니까 while 조건으로는 right가 큰 동안, left가 작은 동안
index 마지막 벗어나지 않게
엇갈릴 때 left right를 교체하는게 아니라 left pivot를 교체하는 것(left 교체)
pivot은 고정(변하지 않음)
pivot은 포함하지 않고 다음 분할(right 기준으로 +1 -1)
'''
array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    start = 0
    end = -1
    pivot = start
    left=pivot+1
    right=end
    while left<=right:
        while array[pivot]>=array[left] and end>=left:
            left +=1
        while array[pivot]<=array[right] and start<right:
            right -=1
        if left>right:
            array[left],array[pivot] = array[pivot],array[left]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array,start,left-1)
    quick_sort(array,left+1,end)


