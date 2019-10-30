def find_duplicates(lst):
    indexlst=[0]*(len(lst))
    outputlst=[]
    for i in range(len(lst)):
        if indexlst[lst[i]]!=-1:
            if indexlst[lst[i]]==lst[i]:
                indexlst[lst[i]]=-1
                outputlst.append(lst[i])
            elif indexlst[lst[i]]==0:
                indexlst[lst[i]]=lst[i]
    return outputlst
