#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

def shift(lst,k):
    for position in range(k):
        lst.append(lst[0])
        lst.pop(0)
