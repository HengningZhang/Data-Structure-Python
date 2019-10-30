def vc_count(word,low,high):
    if low>high:
        return(0,0)
    elif word[low] in "aeiouAEIOU":
        return (vc_count(word,low+1,high)[0]+1,vc_count(word,low+1,high)[1])
    else:
        return (vc_count(word,low+1,high)[0],vc_count(word,low+1,high)[1]+1)
        
