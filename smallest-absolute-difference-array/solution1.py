def solution(A):

    #  we dont need to sum all of the left and right split on each iteration.
    #  If we have total in each iteration we can add new item to first split 
    #  and calculate the other one.
    total = sum(A)
    min_value=float('inf')
    for i in range(len(A)-1):
        split1 += A[i]
        split2=total-split1
        value=abs(split2-split1)
        if value<min_value:
            min_value=value
    return min_value