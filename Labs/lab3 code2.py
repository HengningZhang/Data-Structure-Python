def is_palindrome(s):
    string = ""
    for i in range(len(s)//2):
        string+=s[len(s)-1-i]
    if string == s[0:len(s)//2]:
        return True
    else:
        return False

print(is_palindrome("12322"))

      
