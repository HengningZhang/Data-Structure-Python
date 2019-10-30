def find_min(lst,low,high):
    if low==high:
        return low
    if lst[low]>lst[high]:
        return find_min(lst,low+1,high)
    else:
        return find_min(lst,low,high-1)

def find_second_min(lst,low,high):
    minimal=find_min(lst,low,high)
    if minimal==high:
        return lst[find_min(lst,low,minimal-1)]
    else:
        return min(lst[find_min(lst,low,minimal-1)],lst[find_min(lst,minimal+1,high)])

print(find_second_min([13,9,16,3,4,2,1],0,6))
