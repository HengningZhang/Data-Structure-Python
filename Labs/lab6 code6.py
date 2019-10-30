def split_parity(lst,low=0,high=-1):
    if high==-1:
        high=len(lst)-1
    if low>=high:
        return lst
    elif lst[low]%2==0:
        return split_parity(lst,low+1,high)
    elif lst[low]%2!=0:
        if lst[high]%2==0:
            lst[low],lst[high]=lst[high],lst[low]
            return split_parity(lst,low+1,high-1)
        else:
            return split_parity(lst,low,high-1)
lst = [4, -5, 2, 3, -1, -6, 7, 9, 0]
split_parity(lst)
print(lst)
