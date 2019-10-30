#Hengning Zhang
#CS1134
#HW2
#2019.2.20
def e_approx(n):
    e = 1
    nextone=1
    for i in range(1,n+1):
        nextone/=i
        e+=nextone
    return e

