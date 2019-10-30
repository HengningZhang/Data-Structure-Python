def jump_search(lst,val,k):
    position = 0
    while position<len(lst):
        print(position)
        if val>lst[position]:
            position+=k
            
        elif val<=lst[position]:
            for i in range(position-k,position+1):
                if val == lst[position]:
                    return position
            return None
    if len(lst)//k!=0:
        for i in range(k*(len(lst)//k),len(lst)):
            if lst[i]==val:
                return i
    return None

print(jump_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],15,4))



    
            
            
