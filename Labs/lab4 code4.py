def exponential_search(lst,val):
    if lst[0]==val:
        return 0
    start = 1
    end = 2
    while val>lst[start] and start<len(lst)-1:
        print(start,end)
        if lst[start]==val:
            return start
        else:
            start=end
            end*=2
    if start>len(lst):
        return None
    elif end>len(lst):
        end=len(lst)-1
        
    while (end-start)>1:
        print(start,end)
        if val<lst[(end+start+1)//2]:
            end = (end+start+1)//2
        elif val>lst[(end+start+1)//2]:
            start = (end+start+1)//2
        else:
            return (end+start+1)//2
    if val==lst[start]:
        return start
    elif val==lst[end]:
        return end
    return None

lst = [-1111, -646, -818, -50, -25, -3, 0, 1, 2, 11, 33, 45, 46, 51,
58, 72, 74, 75, 99, 110, 120, 121, 345, 400, 500, 999, 1000, 1114,
1134, 10010, 500000, 999999]
print(exponential_search(lst,110))
