class pais:
    def __init__(self):
        self.name = "Argentina"
        self.population = 500000000
        self.sup = 233432432
        self.capital = "caba"
        self.football_teams = [{"name":"Boca"},{"name":"San Lorenzo"},{"name":"River"}]
        self.bestCountryEver = True

# def toDict(self): #Convertir obj a dict sin reflection, teniendo q escribir 1x1
#     x = {}
#     x["name"]="Argentina"
#     x["population"]=50000000000


# def toDict(): #Con Reflection
#Funcion que nos permite saber si algo es invocable o no: callable(param)
#Limpiamos el dir() de lo que nos tiene que aparecer y lo que no.

    def toDict(self):
        param_list = dir(self)
        attr_dict = {}
        for attr in param_list:
            if (attr.startswith("__") and attr.endswith("__")) or callable(getattr(self,attr)): #Devuelve el value del atributo getattr(self,attr)
                pass
            else:
                attr_dict[attr] = getattr(self,attr)
        return attr_dict


    def fromDict(self,data):
        for key in data.keys():
            setattr(self, key, data[key]) #settea al objeto que le pasas, el atributo que queres q le ponga con el valor.