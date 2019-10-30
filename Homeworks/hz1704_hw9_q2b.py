from ChainingHashTableMap import ChainingHashTableMap
def intersection_list(lst1,lst2):
    output=[]
    table=ChainingHashTableMap()
    for element in lst1:
        table[element]=1
    for element in lst2:
        #if element in table:
        try:
            table[element]*=1
            output.append(element)
        except:
            a=1
    return output


