class MoreThanAList:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
    
        if  len(self.value) > 0:    
            return self.value.pop() 
        else:
            raise StopIteration

myList =  MoreThanAList([1,2,3,4])
for i in myList:
    print(i)