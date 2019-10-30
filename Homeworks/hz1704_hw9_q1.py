from ChainingHashTableMap import ChainingHashTableMap
def intersection_list(lst1,lst2):
    output=[]
    table=ChainingHashTableMap()
    for element in lst1:
        table[element]=1
    for element in lst2:
        if element in table:
            output.append(element)
    return output


print(intersection_list([3, 9, 2, 7, 1], [4, 1, 8, 2]))
