#Hengning Zhang
#CS1134
#HW2
#2019.2.20
def factors(num):
    for i in range(1,int(num**0.5)):
        if num%i==0:
            yield i
    for i in range(int(num**0.5),0,-1):
        if num%i==0:
            yield num//i

