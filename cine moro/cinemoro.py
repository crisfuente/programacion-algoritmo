Texto =""
total=0
total2=0
total3=0
Tniño=0
Tjoven=0
Tadulto=0
print("HOLA")
print("Sea bienvenido al cine moro.")

while Texto !="salir":

 print("-----------------------------------") 
 print("Entrada niños $5.500 [Edad>1-13<]")
 print()
 print("Entrada joven $7.000 [Edad>14-21<]")
 print()
 print("Entada Adulto $9.000 [Edad>Mayor a 22<]")
 print("-----------------------------------")
 print()
 edad=int(input("Por favor digite su edad. "))


 if edad >= 1 and edad <= 13:
  print("Su edad esta en la categoria de >[Niño]<")
  
  entrada=int(input("Ingrese la cantidad de entradas que desea: "))
  Tniño = entrada + entrada
  entrada = entrada * 5500
  total = entrada + entrada
  print(f"El total de las entradas es: ${entrada}")
  print("Si desea continuar escriba [Si]")
  Texto=input("Si desea salir escriba en el teclado [Salir]: ")
  
  

 elif edad >= 14 and edad <=21:
   print("Su edad esta en la categoria de >[Joven]<")
  
   entrada=int(input("Ingrese la cantidad de entradas que desea: "))
   Tjoven = entrada + entrada 
   entrada = entrada * 7000
   total2= entrada + entrada
   print(f"El total de las entradas es: ${entrada}")
   print("Si desea continuar escriba [Si]")
   Texto=input("Si desea salir escriba en el teclado [Salir]: ")
   

 if edad == 0 or edad < 0:
    print("ERROR: esta categoria no existe.")
 
   

 elif edad >= 22 and edad <= 125:
   print("Su edad esta en la categoria de >[Adulto]<")
   entrada=int(input("Ingrese la cantidad de entradas que desea: "))
   Tadulto = entrada + entrada
   entrada = entrada * 9000
   total3= entrada + entrada
   print(f"El total de las entradas es: ${entrada}")
   print("Si desea continuar escriba [Si] ")
   Texto=input("Si desea salir escriba en el teclado [Salir]: ")
   

print()
print(" TOTAL DE VENTAS, FINAL DE LA JORNADA.")
print("-----------------------------------")
totalf = total + total2 + total3
venta = Tniño + Tjoven + Tadulto
por1=Tniño*100/venta
por2=Tjoven*100/venta
por3=Tadulto*100/venta
print("Total de entradas vendidas por categoria.")
print()
print(f"Total de entradas vendidas  [niño]: ${total} ")
print(f"Porcentaje de categoria [Niño]: {int(por1)}%")
print()
print(f"Total de entradas vendidas [Joven]: ${total2} ")
print(f"Porcentaje de categoria [Joven]: {int(por2)}%")
print()
print(f"Total de entradas vendidas [Adulto]: ${total3} ")
print(f"Porcentaje de categoria [Adulto]: {int(por3)}% ")
print()
print(f"Total de entradas vendidas: ${totalf} ")
print("-----------------------------------")