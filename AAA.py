print("---Juegos Triple AAA---")

Game={
   1:"Wolverine",2:"Batman Lego",3:"ResidentEvil Requiem",4:"Star Citizen"
}

def agregarJuegos():
   print("-"*20)
   agregar=input("Ingrese un Juego Triple A: ")
   nuevoKey=list(Game.keys())[-1]
   Game[nuevoKey+1]=agregar
def mostrarJuegos():
   print("-"*40)
   for num, nombre in Game.items():
         print(f"{num}.- {nombre} ")
def eliminarJuegos():
   mostrarJuegos()
   borrar=int(input("Cual Juego borrará?: "))
   del Game[borrar]
def actualizarJuegos():
   mostrarJuegos()
   act=int(input("Cual Juego actualizará?: "))
   Game[act]=input("Ingrese nuevo nombre: ")

def JuegosMenu():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Juego")
         print("2.- Eliminar Juego")
         print("3.- Actualizar Juego")
         print("4.- Mostrar Juegos")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarJuegos()
               case 2:
                  eliminarJuegos()
               case 3:
                  actualizarJuegos()
               case 4:
                  mostrarJuegos()
               case 5:
                  print("Salir")
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)

# vegetalesMenu()

##Diccionario con diccionarios
productosDicc={
   1:{"nombre": "Wolverine", "precio": 3000},
   2:{"nombre": "StarCitizen", "precio": 1500},
   3:{"nombre": "Red Dead Redeption II", "precio": 1200}
}
productosDicc[4]={"nombre": "Red Dead Redeption II", "precio": 3500}
def agregarProducto():
   print("Cual es el nombre del Juego?")
   nombre = input()
   print("cual es el precio?")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())[-1]
   productosDicc[nuevoKey+1]= {"nombre": nombre, "precio": precio}
def MostrarProducto():
   for key, producto in productosDicc.items():
      print(f"{key} .{producto}")
def eliminarProducto():
   MostrarProducto()
   borrar=int(input("Cual Producto borrará?: "))
   del productosDicc[borrar]
def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))

   nombre=input("Cual es el nombre nuevo?: ")
   precio=int(input("Cual es el precio nuevo?: "))
   productosDicc[num]={"nombre": nombre, "precio": precio}
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla

# for num, veg in productosDicc.items():
#     print(f"{num}.- {veg}")

##Lista con diccionarios
productosList=[
   {"nombre": "Wolverine", "precio": 3000}, #0
   {"nombre": "StarCitizen", "precio": 1500},     #1  
   {"nombre": "Red Dead Redeption II", "precio": 1200}   #2
]

print(productosList[2]["precio"]) #precio de la cebolla
print(productosList[0]["nombre"]) #nombre de la naracuya



def JuegosMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Juego")
         print("2.- Eliminar Juego")
         print("3.- Actualizar Juego")
         print("4.- Mostrar Juegos")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                  print("Salir")
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)


