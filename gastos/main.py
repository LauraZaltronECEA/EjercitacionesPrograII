from tabulate import tabulate

gastos  = [
    {"categoria":"comida","monto":120000},
    {"categoria":"transporte","monto":3000},
    {"categoria":"comida","monto":30000},
    {"categoria":"ocio","monto":50000},
    {"categoria":"transporte","monto":50000},
    {"categoria":"mascotas","monto":20000},
    {"categoria":"ocio","monto":50000}
]

totales = []
parciales = {} #Diccionario para almacenar los totales parciales por categoria.

for gasto in gastos:
    try:
        parciales[gasto["categoria"]] += gasto["monto"] #Si la categoria ya existe, se suma el monto al total parcial.
    except KeyError:
        parciales[gasto["categoria"]] = gasto["monto"]#Si la categoria no existe, se crea una nueva entrada en el diccionario con el monto del gasto.

for categoria in parciales.keys():
    totales.append([categoria, parciales[categoria]])

print(tabulate(totales, headers=["Categoria", "Total"]))

#Abrir VENV, importar tabulate, ejecutar main.py.