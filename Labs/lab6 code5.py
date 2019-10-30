def binary_search(lst,val,low,high):
    if lst[(high+low)//2]==val:
        return (high+low)//2
    elif lst[(high+low)//2]<val:
        return binary_search(lst,val,(high+low)//2+1,high)
    else:
        return binary_search(lst,val,low,(high+low)//2)

print(binary_search([1,2,3,4,5,6,7],5,0,6))
