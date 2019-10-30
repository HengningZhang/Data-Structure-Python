#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

def fibs(n):
    lst=[1,1]
    if n==1:
        return [1]
    elif n==2:
        return ["1 1"]
    else:
        for position in range(2,n):
            lst.append(lst[position-2]+lst[position-1])
        for position in range(len(lst)):
            lst[position]=str(lst[position])
            
        generator = " ".join(lst)
        return [generator]
