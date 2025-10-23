def calculate_time_min(enter, left):
    final_min=0
    hour_enter=int(enter[0:2])
    hour_left=int(left[0:2])
    min_enter=int(enter[3:5])
    min_left=int(left[3:5])
    final_min=final_min+(hour_left-hour_enter)*60

    if min_left>=min_enter:
        final_min=final_min+(min_left-min_enter)
    else:
        final_min=final_min+(min_left-(min_enter-60))
        final_min-=60
    return final_min
        
# calculate price from duration of stay (min)
def calculate_price(time_min):
    price=5
    if time_min>60:
        hours=(time_min-60)//60
        partial_mins=abs(time_min-60-(hours)*60)
        if partial_mins>0:
            hours+=1
        price=price+(hours)*4
    return price


def solution(E, L):
    time_min=calculate_time_min(E,L)
    price=calculate_price(time_min)
    return price

price=solution(input("Provide Enterance Time in HH:MM format:"), input("Provide Exit Time in HH:MM format:"))
print(str(price)+"$")