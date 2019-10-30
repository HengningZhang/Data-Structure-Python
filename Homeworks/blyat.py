from ChainingHashTableMap import ChainingHashTableMap

def blyat(lst):
    table=ChainingHashTableMap()
    for i in range(len(lst)):
        if lst[i] not in table:
            table[lst[i]]=i
    return table
for i in blyat([5,9,2,9,0,5,9,7]):
    print(i)
