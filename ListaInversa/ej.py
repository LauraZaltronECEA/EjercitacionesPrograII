class MoreThanAList:# clase que se comporta como una lista pero con un iterador personalizado
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
    
        if  len(self.value) > 0:    
            return self.value.pop()
        else:
            raise StopIteration

#el iterador personalizado devuelve los elementos de la lista en orden inverso,
#ya que se utiliza el método pop()
#que elimina y devuelve el último elemento de la lista.
myList =  MoreThanAList([1,2,3,4])
for i in myList:
    print(i)