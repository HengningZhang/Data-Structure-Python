def is_palindrome(input_str,low,high):
    if low>=high:
        return True
    elif input_str[low]!=input_str[high]:
        return False
    else:
        return is_palindrome(input_str,low+1,high-1)

print(is_palindrome("racecar",0,5))
