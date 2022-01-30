words=	["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=  ["fro??", "????o", "fr???", "fro???", "pro?"]

'''
접두사 아니면 접미사로만 주어지기 때문에 시작점을 구할수 있을지도
맨 뒤를 ? 기준으로
1.찾았는데 더 앞이거나
2.못찾았는데 뒤이거나
3.딱 거기
'''
def solution_1():
    answer = []
    for i in range(len(queries)): # 일단 fro?? 에서 ? 위치를 찾기
        ret_f = -1
        ret_b = -1
        cnt=0
        if queries[i][0]=='?': #?rodo
            mid=(len(queries[i])-1)//2
            ret_f = bs(queries[i],0,len(queries[i])-1,+1)
        else :                  #frod?
            mid=(len(queries[i])-1)//2
            ret_b = bs(queries[i],0,len(queries[i])-1,-1)

        if ret_f!=-1: # 앞쪽 ?를  찾은 경우... 난 ㅠㅠ앞쪽 단어라고 착각..
            find=queries[i][ret_f+1:]
        else: # 뒷쪽 ? 찾은 경우
            find = queries[i][:ret_b]
        for w in words:
            if ret_f!=-1:
                if find in w[ret_f+1:]: #앗! 글자만 들어가면 되는게 아니라, 위치도 생각해야 하네
                    if len(w) == len(queries[i]):
                        cnt += 1
            else:
                if find in w[:ret_b]:
                    if len(w) == len(queries[i]):
                        cnt+=1
        answer.append(cnt)
    print(answer)
    return answer

def bs(q,start,end,dir):
    if start>end: #무조건 있으니까 없어도..?
        return None
    mid=(start+end)//2
    #tmp_mid=mid+dir # 1개 뒤로 이동이 안되네...
    if '?'==q[mid]:
        if q[mid+dir]=='?': #왜 인덱스 에러가... #뒤로갔는데 있을 떄
            #if mid+dir%2!=0:
                #tmp_mid=mid+dir+1
            if dir==1: #앞에서 ?시작한 경우 ???do
                return bs(q,mid+1,end,dir)
            else : # 뒤에서 ? 시작한 경우 fro??
                return bs(q,start,mid-1,dir)
        else :
            return mid
    elif '?' != q[mid]:
        if dir==1: #  ?~~
            return bs(q,start,mid-1,dir)
        else : # ~~?
            return bs(q,mid+1,end, dir)

solution_1()