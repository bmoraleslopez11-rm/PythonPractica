# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# # print(alumno)
# # print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

productos={
    1:{"nombre": "Control Inalambrico",
       "categoria": "Electronica",
       "precio": 45000},
    2:{"nombre": "Pilas Recargables",
       "categoria": "Insumos",
       "precio": 5000},
    3:{"nombre": "Pasta Termica",
       "categoria": "Computacion",
       "precio": 7000},
}

print(productos[1]["nombre"])

'''
Crear un diccionario de trabajadores 
'''

##CRUD DE VEGETALES

vegetales={
   1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
}

print(list(vegetales.keys())[-1])


def agregarVegetales():
   print("-"*20)
   agregar=input("Ingrese un vegetal: ")
   nuevoKey=list(vegetales.keys())[-1]
   vegetales[nuevoKey+1]=agregar
def mostrarVegetales():
   print("-"*40)
   for num, nombre in vegetales.items():
         print(f"{num}.- {nombre} ")
def eliminarVegetal():
   mostrarVegetales()
   borrar=int(input("Cual vegetal borrará?: "))
   del vegetales[borrar]
def actualizarVegetal():
   mostrarVegetales()
   act=int(input("Cual vegetal actualizará?: "))
   vegetales[act]=input("Ingrese nuevo nombre: ")

def vegetalesMenu():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarVegetales()
               case 2:
                  eliminarVegetal()
               case 3:
                  actualizarVegetal()
               case 4:
                  mostrarVegetales()
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
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
productosDicc[4]={"nombre": "Piña", "precio": 3500}
def agregarProducto():
   print("Cual es el nombre del producto?")
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
   {"nombre": "Maracuyá", "precio": 3000}, #0
   {"nombre": "Pera", "precio": 1500},     #1  
   {"nombre": "Cebolla", "precio": 1200}   #2
]

print(productosList[2]["precio"]) #precio de la cebolla
print(productosList[0]["nombre"]) #nombre de la naracuya



carrito=[]
def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear boleta y salir")
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
vegetalesMenuDiccionario()

#Cambiar la funcion actualizar para que solo 
# actualice una solo key 
# Ademas, crear un CRUD pero con la lista 
# de diccionarios.
