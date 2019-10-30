#Hengning Zhang
#CS 1134
#HW 2
#2019/2/19
def findChange(lst01):
    start = 0
    end = len(lst01)
    while len(lst01)>1:
        if lst01[(end-start)//2]==0 or lst01[(end-start)//2-1]==0:
            lst01=lst01[(end-start)//2:]
            start = (start+end)//2
        else:
            lst01=lst01[:(end-start)//2]
            end= (start+end)//2
    return start

