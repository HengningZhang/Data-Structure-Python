import ArrayQueue
def n_bonacci(n,k):
    q=ArrayQueue.ArrayQueue()
    output=0
    for i in range(k):
        if i<n:
            q.enqueue(1)
            output+=1
            yield 1
        else:
            yield output
            q.enqueue(output)
            output=2*output-q.dequeue()
            


    
