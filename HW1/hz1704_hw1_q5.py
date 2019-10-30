#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

def fibs(n):
    lst=[1,1]
    if n==1:
        yield 1
    elif n==2:
        yield 1
        yield 1
    else:
        yield 1
        yield 1
        for position in range(2,n):
            lst.append(lst[position-2]+lst[position-1])
            yield lst[position]


