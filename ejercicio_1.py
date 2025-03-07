("print==================================")
print("====MOSTRAR NOMBRE EN PANTALLA==== ")
("print==================================")

# definicion de la funcion 
def mostrarNombre(nombre):
    for i in range(1, 6):
        print(f"{i} . {nombre}")

# intput

nombre = input("Digite su nombre: ")

# processing 
mostrarNombre(nombre)

# salida
print("\nEso era...")