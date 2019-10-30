#Hengning Zhang
#CS 1134
#HW 2
#2019/2/19
def two_sum(srt_lst,target):
    left = 0
    right = len(srt_lst)-1
    while left<right:
        if target>srt_lst[left]+srt_lst[right]:
            left+=1
        elif target<srt_lst[left]+srt_lst[right]:
            right-=1
        else:
            return (left,right)
    return None

