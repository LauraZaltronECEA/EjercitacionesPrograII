try:
    raise StopIterarion("Parar de correr") #tirar una exception a proposito, con un mensaje para que no tire error el e.args
    #- Por default las excepciones que tiramos no tienen mensaje
    "Hola"**2 #TypeError
    1/0 #ZeroDivError
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Error de tipo")
except Exception as e:
    print("Ocurrio un error: {}".format(e.args[0]))
finally:
    print("Esto se eejcuta si o si.")
#Todas las excepciones heredan de la clase Exception
#StopIterarion es un tipo de iteracion utilizada en el for.