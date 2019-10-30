def permutation(lst):
    if len(lst)==0:
        return None
    elif len(lst)==1:
        return lst
    else:
        factorial=1
        for num in range(1,len(lst)+1):
            factorial*=num
        output = [[]]*factorial
        k = len(lst)
        for outputelement in output:
            for num in lst:
                if num not in outputelement:
                    output.append([a]+b)
        return output
print(permutation([1,2]))

#网上大哥的
def permutation(lst):
    output = [[]]
    k = len(lst)
    for i in range(k):
        output = [[a] + b for a in lst for b in output if a not in b]
    return output



print(permutations([1,2,3]))
