def reverse_list(lst):
    for i in range(len(lst)//2):
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],lst[i]
    return lst

lst = [1,2,3,4]
reverse_list(lst)
print(lst)
