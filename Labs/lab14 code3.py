from ChainingHashTableMap import ChainingHashTableMap
def create_palindrome(letters):
    table = ChainingHashTableMap()
    output=""
    for i in letters:
        try:
            table[i]+=1
        except:
            table[i]=1
    for i in table:
        output+=i*(table[i]//2)
        if table[i]%2==1:
            add=i
    try:
        output+=add
        if len(output)!=1:
            
            output+=output[-1::-1]
    except:
        output+=output[::-1]

    print(output)

create_palindrome( "aaaabbccccddde")
        
        
        
create_palindrome("wxyzwxyz")
create_palindrome("abcdefg")
