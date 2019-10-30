import ArrayStack

def arithmetic(lst):
    operators="+-*/"
    calcstack = ArrayStack.ArrayStack()
    for element in lst:
        if element not in operators:
            calcstack.push(int(element))
        else:
            secondnum=calcstack.pop()
            firstnum=calcstack.pop()
            if element=="+":
                result=firstnum+secondnum
            elif element=="-":
                result=firstnum-secondnum
            elif element=="*":
                result=firstnum*secondnum
            else:
                result=firstnum/secondnum
            calcstack.push(result)
    return calcstack.pop()

def main():
    dct={}
    inputstring=""
    while True:
        inputstring=input("-->")
        if inputstring == "done()":
            return
        lst = inputstring.split(" ")
        for i in range(len(lst)):
            if lst[i] in dct:
                lst[i]=str(dct[lst[i]])
        if len(lst)==1:
            print(lst[0])     
        elif "=" in lst:
            dct[lst[0]]= arithmetic(lst[2:])
            print(lst[0])
        else:
            print(arithmetic(lst))
main()
            
        
