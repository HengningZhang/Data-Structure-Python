def create_permutation(n):
    import random
    lst=[]
    for num in range(n):
        lst.append(num)
    randlst=[]
    while len(lst)>0:
        choice=random.randint(0,len(lst)-1)
        randlst.append(lst[choice])
        lst.pop(choice)
        
    return randlst
        
            
def scramble_word(word):
    import random
    order=create_permutation(len(word))
    lst=[]
    scramblestring=""
    for element in order:
        scramblestring+=word[element]
    return scramblestring

def guessgame(word):
    scrambledword=scramble_word(word)
    print("Unscramble the word:",end="")
    for char in scrambledword:
        print(char,end=" ")
    print()
    userinput=input("Try #1:")
    attempt = 2
    while userinput!=word:
        print("Wrong!")
        userinput=input("Try #"+str(attempt)+":")
        attempt+=1
    print("Yay, you got it!")
    return True
        
guessgame("Pokemon")
