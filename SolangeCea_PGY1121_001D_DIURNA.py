import os
os.system("cls")
print("""Cracol Express
       Opcion 1) Ingresar Encomienda 
       Opcion 2) Buscar Encomienda 
       Opcion 3) Mostrar Encomiendas
       Opcion 4) Salir        
       """)

opcion = int(input("Ingrese opción:  "))
listaEncomienda = []
listaDatos = []
while True:
    for i in range (1):
     try:
      if opcion == 1:
       encomienda = input("ingresa una encomienda:")
       listaEncomienda.append(encomienda)
       tipo = input("Ingrese tipo de encomienda:  ")
       nomDes = input("Ingrese nombre destinatario:  ")
       rutDes = input("Ingrese rut destinatario: ")
       pesoKg= input ("Ingrese peso en Kg: ")
       precio = input ("Ingrese precio: ")
       ciudad = input ("Ingrese ciudad de destino: ")

       listaDatos.append(tipo,nomDes,rutDes,pesoKg,precio,ciudad)
      elif opcion == 3:
       print(f"{listaEncomienda}")
       break
     except:
      print("Ingrese Opcion valida")
    break
while True: 
    try:
     if opcion==2:
      RutBusc = input("Ingrese rut: ")
     elif RutBusc == rutDes:
      print("")
      break
    except:
     print("Ingrese opcion valida")
     break

     
 