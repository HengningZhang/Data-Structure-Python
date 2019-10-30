import time
import random
class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

'''
Linear maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0
    
    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0

    return maxSum, seqStart, seqEnd


'''
Quadratic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd


'''
Cubic maximum contiguous subsequence sum algorithm.
seqStart and seqEnd represent the actual best sequence.
'''
def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd

def test():
    t = PolyTimer()
    nuClicks = 0.0
    lst=[]
    for i in range(7,13):
        for i in range(2**i):
            lst.append(random.randint(-1000,1000))

    result, start, end = maxSubsequenceSum1(lst)
    nuClicks = t.elapsed()
    t.reset()
    f = open("test.csv","w")
    print(nuClicks,file=f)
    result, start, end = maxSubsequenceSum2(lst)
    nuClicks = t.elapsed()
    t.reset()
    print(nuClicks,file=f)
    result, start, end = maxSubsequenceSum3(lst)
    nuClicks = t.elapsed()
    t.reset()
    print(nuClicks,file=f)
    f.close()
    

test()
