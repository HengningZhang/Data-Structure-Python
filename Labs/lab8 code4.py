class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]
def is_balanced(input_str):
    s = ArrayStack()
    if input_str[0] in ")}]":
        return False
    for i in range(len(input_str)):
        if input_str[i] in "({[":
            s.push(input_str[i])
        elif input_str[i] == ")":
            if s.top()=="(":
                s.pop()
            else:
                return False
        if input_str[i] == "]":
            if s.top()=="[":
                s.pop()
            else:
                return False
        if input_str[i] == "}":
            if s.top()=="{":
                s.pop()
            else:
                return False
        
    if len(s)!=0:
        return False
    return True
print(is_balanced(("(([]{{[]}})")))
    
