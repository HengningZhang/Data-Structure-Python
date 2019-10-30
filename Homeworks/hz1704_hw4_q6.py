def appearances(s,low,high):
    if low>high:
        return {}
    dct=appearances(s,low+1,high)
    if s[low] not in dct:
        dct[s[low]]=1
    else:
        dct[s[low]]+=1
    return dct

