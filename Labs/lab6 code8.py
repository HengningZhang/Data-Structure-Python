def nested_sum_helper(lst,low,high=-1):
    if high==-1:
        high = len(lst)-1
    if low>high:
        return 0
    if isinstance(lst[low],int):
        return lst[low]+ nested_sum_helper(lst,low+1,high)
    else:
        return nested_sum_helper(lst[low],0,len(lst[low])-1)+ nested_sum_helper(lst,low+1,high)

def nested_sum(lst):
    low=0
    high=len(lst)-1
    return nested_sum_helper(lst,low,high)
print(nested_sum([ [1, 2], 3, [4, [5, 6, [7], 8 ] ] ]))
