def remove_all(lst,elem):
    elemcounter=0
    for i in range(len(lst)):
        if lst[i]==elem:
            elemcounter+=1
        else:
            lst[i-elemcounter]=lst[i]
    for i in range(elemcounter):
        lst.pop()

    
