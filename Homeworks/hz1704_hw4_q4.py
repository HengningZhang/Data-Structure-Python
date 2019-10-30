def list_min(lst,low,high):
    if low==high:
        return lst[low]
    elif lst[low]>lst[high]:
        return list_min(lst,low+1,high)
    elif lst[low]<lst[high]:
        return list_min(lst,low,high-1)

