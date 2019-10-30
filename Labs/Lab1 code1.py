def add_binary(bin_num1,bin_num2):
    len1=len(bin_num1)-1
    len2=len(bin_num2)-1
    num1=0
    num2=0
    for bit in bin_num1:
        num1+=int(bit)*2**len1
        len1-=1
    for bit in bin_num2:
        num2+=int(bit)*2**len2
        len2-=1
    thesum=num1+num2
    binsum=""
    while thesum>0:
        binsum=str(thesum%2)+binsum
        thesum//=2
    return binsum

print(add_binary("11","1"))

        
        
