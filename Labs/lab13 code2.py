from ChainingHashTableMap import ChainingHashTableMap
def two_sum(lst,target):
    table=ChainingHashTableMap()
    for i in range(len(lst)):
        if lst[i] not in table:
            table[lst[i]]=i
    for element in lst:
        if (target-element) in table:
            if element!=(target-element):
                return (table[element],table[target-element])
    return (None,None)

print(two_sum([-2, 11, 15, 21, 20, 7],22))
                    
