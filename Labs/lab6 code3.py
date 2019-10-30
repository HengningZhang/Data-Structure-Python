def find_max(lst,low,high):
    if low==high:
        return lst[low]
    elif lst[low]<lst[high]:
        return find_max(lst,low+1,high)
    elif lst[low]>lst[high]:
        return find_max(lst,low,high-1)

print(find_max([13,9,16,3,4,2],0,5))
