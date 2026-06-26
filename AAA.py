# print("---Juegos Triple AAA---")

# Game={
#    1:"Wolverine",2:"Batman Lego",3:"ResidentEvil Requiem",4:"Star Citizen"
# }

# def agregarJuegos():
#    print("-"*20)
#    agregar=input("Ingrese un Juego Triple A: ")
#    nuevoKey=list(Game.keys())[-1]
#    Game[nuevoKey+1]=agregar
# def mostrarJuegos():
#    print("-"*40)
#    for num, nombre in Game.items():
#          print(f"{num}.- {nombre} ")
# def eliminarJuegos():
#    mostrarJuegos()
#    borrar=int(input("Cual Juego borrará?: "))
#    del Game[borrar]
# def actualizarJuegos():
#    mostrarJuegos()
#    act=int(input("Cual Juego actualizará?: "))
#    Game[act]=input("Ingrese nuevo nombre: ")

# def JuegosMenu():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Juego")
#          print("2.- Eliminar Juego")
#          print("3.- Actualizar Juego")
#          print("4.- Mostrar Juegos")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarJuegos()
#                case 2:
#                   eliminarJuegos()
#                case 3:
#                   actualizarJuegos()
#                case 4:
#                   mostrarJuegos()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)

# # vegetalesMenu()

# ##Diccionario con diccionarios
# productosDicc={
#    1:{"nombre": "Wolverine", "precio": 3000},
#    2:{"nombre": "StarCitizen", "precio": 1500},
#    3:{"nombre": "Red Dead Redeption II", "precio": 1200}
# }
# productosDicc[4]={"nombre": "Red Dead Redeption II", "precio": 3500}
# def agregarProducto():
#    print("Cual es el nombre del Juego?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())[-1]
#    productosDicc[nuevoKey+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#       print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    borrar=int(input("Cual Producto borrará?: "))
#    del productosDicc[borrar]
# def actualizarProducto():
#    MostrarProducto()
#    num=int(input("Que producto desea actualizar?: "))

#    nombre=input("Cual es el nombre nuevo?: ")
#    precio=int(input("Cual es el precio nuevo?: "))
#    productosDicc[num]={"nombre": nombre, "precio": precio}
# # print(productosDicc[2]["precio"])  # precio de la pera
# # print(productosDicc[3]["nombre"])  # nombre de la cebolla

# # for num, veg in productosDicc.items():
# #     print(f"{num}.- {veg}")

# ##Lista con diccionarios
# productosList=[
#    {"nombre": "Wolverine", "precio": 3000}, #0
#    {"nombre": "StarCitizen", "precio": 1500},     #1  
#    {"nombre": "Red Dead Redeption II", "precio": 1200}   #2
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya



# def JuegosMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Juego")
#          print("2.- Eliminar Juego")
#          print("3.- Actualizar Juego")
#          print("4.- Mostrar Juegos")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarProducto()
#                case 2:
#                   eliminarProducto()
#                case 3:
#                   actualizarProducto()
#                case 4:
#                   MostrarProducto()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)






# Lista principal de productos
productos = []

# ---------------- VALIDACIONES ----------------

def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_stock(stock):
    try:
        stock = int(stock)
        return stock >= 0
    except:
        return False


def validar_precio(precio):
    try:
        precio = float(precio)
        return precio > 0
    except:
        return False


# ---------------- MENÚ ----------------

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar un número entre 1 y 6.")
        except:
            print("Debe ingresar un número válido.")


# ---------------- OPCIÓN 1 ----------------

def agregar_producto(lista):
    nombre = input("Nombre del producto: ")

    if validar_nombre(nombre) == False:
        print("Error: El nombre no puede estar vacío.")
        return

    stock = input("Stock: ")

    if validar_stock(stock) == False:
        print("Error: El stock debe ser un número entero mayor o igual a 0.")
        return

    precio = input("Precio: ")

    if validar_precio(precio) == False:
        print("Error: El precio debe ser un número mayor que 0.")
        return

    producto = {
        "nombre": nombre,
        "stock": int(stock),
        "precio": float(precio),
        "disponible": False
    }

    lista.append(producto)
    print("Producto agregado correctamente.")


# ---------------- OPCIÓN 2 ----------------

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i
    return -1


# ---------------- OPCIÓN 4 ----------------

def actualizar_disponibilidad(lista):
    for producto in lista:
        if producto["stock"] > 0:
            producto["disponible"]= True
        else:
            producto["disponible"] = False


# ---------------- PROGRAMA PRINCIPAL ----------------

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_producto(productos)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del producto: ")
        lugar = buscar_producto(productos, nombre)

        if lugar != -1:
            print("Producto encontrado en la posición", lugar)
            print("Nombre:", productos[lugar]["nombre"])
            print("Stock:", productos[lugar]["stock"])
            print("Precio:", productos[lugar]["precio"])
            print("Disponible:", productos[lugar]["disponible"])
        else:
            print("Producto no encontrado.")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        lugar = buscar_producto(productos, nombre)

        if lugar != -1:
            del productos[lugar]
            print("Producto eliminado correctamente.")
        else:
            print("El producto", nombre, "no se encuentra registrado.")

    elif opcion == 4:
        actualizar_disponibilidad(productos)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        actualizar_disponibilidad(productos)

        print("=== LISTA DE PRODUCTOS ===")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print("Nombre:", producto["nombre"])
                print("Stock:", producto["stock"])
                print("Precio:", producto["precio"])

                if producto["disponible"] == True:
                    print("Estado: DISPONIBLE")
                else:
                    print("Estado: SIN STOCK")

                print("*" * 45)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break