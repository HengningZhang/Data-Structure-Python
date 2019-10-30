def partition(lst,low,high):
    pivot=lst[low]
    count=0
    for i in range(low,high+1):
        if lst[i]<pivot:
            count+=1
    return count

def mutate(lst,low,high,pivot):
    count=0
    for position in range(low,high+1):
        if lst[position]<pivot:
            lst[position-count],lst[position]=lst[position],lst[position-count]
        else:
            count+=1
        
def quick_sort(lst,low,high):
    if low>=high:
        return
    
    position=partition(lst,low,high)+low
    lst[low],lst[position]=lst[position],lst[low]
    if high-low>1:
        mutate(lst,low,high,lst[position])
    quick_sort(lst,low,position-1)
    quick_sort(lst,position+1,high)

lst=[54, 31, 77, 55, 17, 20, 44, 93, 26]
quick_sort(lst,0,8)

print(lst)
