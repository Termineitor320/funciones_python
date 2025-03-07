print("================================")
print("==BUSCAR UN NUMERO EN CONJUNTO==")
print("================================")

# definicion de la funcion 
def buscarDatoEnLista(datoABuscar, lista ):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

# input 
dato = int(input("Numero a buscar: ")) # se recibe el dato  del usuario 

#processing 
lista = [1,2,3,4,5] # se almacena una lista de datos 
if buscarDatoEnLista(dato, lista ):
    print("lo encontre")
else:
    print("no lo encontre ")

