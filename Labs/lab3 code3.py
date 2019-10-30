def move_zeroes(nums):
    newlist=[]
    zerocounter=0
    for i in range(len(nums)):
        if nums[i]!=0:
            newlist+=[i]

    for i in range(len(newlist)):
        nums[i]=nums[newlist[i]]
    for i in range(len(newlist),len(nums)):
        nums[i]=0


