#Hengning Zhang
#CS1134
#HW2
#2019.2.20
def split_parity(lst):
    firsteven=0
    for i in range(len(lst)):
        if lst[i]%2!=0:
            lst[i],lst[firsteven]=lst[firsteven],lst[i]
            firsteven+=1

