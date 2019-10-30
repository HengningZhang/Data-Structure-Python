from ChainingHashTableMap import ChainingHashTableMap
def most_frequent(lst):
    if len(lst)==0:
        return None
    
    table=ChainingHashTableMap()
    for element in lst:
        if element not in table:
            table[element]=1
        else:
            table[element]+=1
    maxnum=table[lst[0]]
    maxelem=None
    for key in table:
        if table[key]>=maxnum:
            maxnum=table[key]
            maxelem=key
    return maxelem

print(most_frequent([9,9]))
        
