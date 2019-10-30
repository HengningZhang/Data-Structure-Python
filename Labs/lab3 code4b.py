def find_missing(lst):
   for i in range(len(lst)+1):
       if i != lst[i]:
           return i
