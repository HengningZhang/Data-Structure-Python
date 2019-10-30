#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

def shift(lst,k,direction="left"):
    if direction=="right":
        positions = len(lst)-k%len(lst)
        for position in range(0,positions):
            lst.append(lst[position])
        for junk in range(positions):
            lst.pop(0)
    else:
        for position in range(k%len(lst)):
            lst.append(lst[0])
            lst.pop(0)

