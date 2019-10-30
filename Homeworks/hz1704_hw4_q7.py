def split_by_sign(lst,low,high):
    if low>=high:
        return lst
    elif lst[low]<0:
        return split_by_sign(lst,low+1,high)
    else:
        if lst[high]<0:
            lst[low],lst[high]=lst[high],lst[low]
            return split_by_sign(lst,low+1,high-1)
            
        else:
            return split_by_sign(lst,low,high-1)

        
