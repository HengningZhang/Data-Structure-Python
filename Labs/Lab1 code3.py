def create_permutation(n):
    import random
    lst=[]
    for num in range(n):
        lst.append(num)
    randlst=[]
    while len(lst)>0:
        choice=random.randint(0,len(lst)-1)
        randlst.append(lst[choice])
        lst.pop(choice)
        
    return randlst

print(create_permutation(10))
        
            
