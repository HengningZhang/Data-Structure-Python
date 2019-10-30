def can_construct(word,letters):
    letterlist=[]
    for char in letters:
        letterlist.append(char)
        
    for char in word:
        if char in letterlist:
            letterlist.pop(letterlist.index(char))
        if char not in letterlist:
            return False
    return True
            
print(can_construct("apples","aples"))
