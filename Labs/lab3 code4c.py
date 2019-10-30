def find_missing_n(lst):
    counter=0
    lstcounter=0
    for i in range(len(lst)+1):
        counter+=i
    for i in range(len(lst)):
        lstcounter+=lst[i]
    return counter-lstcounter

print(find_missing_n([8,6,0,4,3,5,1,2]))
