print("================================")
print("==BUSCAR UN NUMERO EN CONJUNTO==")
print("================================")

# entrada
b = int(input("Numero a buscar: ")) # se recibe el dato del usuario 

# processing 
a = [1,2,3,4,5] # se almacena unalista de datos 
r = False  # se inicia la variable r con un valor falso   

for i in a:
    if i==b:
      print("lo encontre")
      r = True 
if r== False:
    print("no lo encontre")
    
# salida 
print("\nEso era...")