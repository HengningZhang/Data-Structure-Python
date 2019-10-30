def reverse_vowels(input_str):
    list_str = list(input_str)
    left = 0
    right = len(list_str)-1
    while right-left>1:
        if list_str[left] not in "aeiou":
            left+=1
        elif list_str[right] not in "aeiou":
            right-=1
        else:
            list_str[left],list_str[right]=list_str[right],list_str[left]
            right-=1
            left+=1
            
    outputstr="".join(list_str)
    return outputstr

print(reverse_vowels("tandon"))
