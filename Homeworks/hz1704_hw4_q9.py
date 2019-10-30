def permutations(lst,low,high):
    if low==high:
        return [[lst[low]]]
    output = permutations(lst,low+1,high)
    length=len(output)*(high-low)
    for element in range(0,length,high-low+1):
        for times in range(high-low):
            output.insert(element,output[element].copy())
            element+=1
    counter=0
    for i in range(len(output)):
        if counter==high-low+1:
            counter=0
        output[i].insert(counter,lst[low])
        counter+=1
    return output

            
                
            
