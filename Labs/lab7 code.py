def partition(lst,pivot):
    count=0
    for i in range(len(lst)):
        if lst[i]<pivot:
            count+=1
    return count

def quick_select(lst,k):
    for i in range(len(lst)):
        if partition(lst,i)==k-1:
            return lst[i]

print(quick_select([1,2,6,4,5,3,7,8,9,0],4))
