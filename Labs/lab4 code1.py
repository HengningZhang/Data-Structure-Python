def str_to_int(int_str):
    length = len(int_str)
    num=0
    for i in range(length):
        num+=int(int_str[i])*10**(length-i-1)
    return num

print(str_to_int("1134"))
