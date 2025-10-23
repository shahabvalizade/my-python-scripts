def solution(A):
    min_value=float('inf')
    for i in range(1,len(A)):
        split1=sum(A[0:i])
        split2=sum(A[i:len(A)])
        value=abs(split2-split1)
        if value<min_value:
            min_value=value
            # add early exit
            if min_value == 0:  # can't do better
                return 0
    return min_value