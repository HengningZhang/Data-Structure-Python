#Hengning Zhang
#CS 1134
#HW 1
#2019/2/2

def squaresum(n):
    thesum=0
    for num in range(n):
        thesum+=num**2
    return thesum

square_sum = sum([num**2 for num in range(5)])

def squaresum_odd(n):
    thesum=0
    for num in range(n):
        if num%2!=0:
            thesum+=num**2
    return thesum

square_sum_odd=sum([num**2 for num in range(5) if num%2!=0])
