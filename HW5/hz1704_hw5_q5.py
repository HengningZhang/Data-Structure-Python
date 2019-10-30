import ArrayQueue
import ArrayStack

def permutations(lst):
    stack=ArrayStack.ArrayStack()
    queue=ArrayQueue.ArrayQueue()
    stack.push([])
    output=[]
    roundnum=1
    while roundnum<=len(lst):
        while len(stack)!=0:
            for num in lst:
                if num not in stack.top():
                    queue.enqueue(stack.top()+[num])
            stack.pop()
        while len(queue)!=0:
            stack.push(queue.dequeue())
        roundnum+=1
    while len(stack)!=0:
        output.append(stack.pop())
    return output


