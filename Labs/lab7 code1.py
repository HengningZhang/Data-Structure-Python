def find_min(lst,low,high):
    if low==high:
        return lst[low]
    if lst[low]>lst[high]:
        return find_min(lst,low+1,high)
    else:
        return find_min(lst,low,high-1)

print(find_min([13,9,16,3,4,2],0,5))
