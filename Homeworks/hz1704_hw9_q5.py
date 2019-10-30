from UnsortedArrayMap import UnsortedArrayMap
class InvertedFile:
    def __init__(self, file_name):
        temp=[]
        temp2=[]
        self.data=UnsortedArrayMap()
        file=open(file_name,"r")
        for line in file:
            temp.append(line)
        for i in range(len(temp)):
            temp[i]=temp[i].split(" ")
        for element in temp:
            for innerelement in element:
                innerelement = innerelement.lower()
                if innerelement!="\n":
                    if "\n" in innerelement:
                        innerelement=innerelement[:-1]
                    if innerelement[-1] in ".,?!;:" :
                        innerelement=innerelement[:-1]

                    temp2.append(innerelement)
        for i in range(len(temp2)):
            try:
                self.data[temp2[i]].append(i)
            except:
                self.data[temp2[i]]=[i]
                
    def indices(self, word):
        try:
            return self.data[word]
        except:
            return []
def main():
    inv_file = InvertedFile("row your boat.txt")
    print(inv_file.indices("row"))

 
