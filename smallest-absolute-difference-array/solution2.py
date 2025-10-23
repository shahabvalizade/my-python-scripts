def solution(A):
    min_value=float('inf')
    for i in range(1,len(A)):
        split1=sum(A[0:i])
        split2=sum(A[i:len(A)])
        value=abs(split2-split1)
        if value<min_value:
            min_value=value
    return min_value