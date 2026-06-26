productos=[]

def validar_nombre(nombre):
    return nombre.strip() !=""

def validar_stock(stock):
    try:
        stock=int(stock)
        return stock>=0
    except:
        return False

def validar_precio(precio):
    try:
        precio=float(precio)
        return precio>0
    except:
        return False

def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar productos")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("Debe ingresar un numero entre 1 y 6")
        except:
            print("Debe ingresar un numero valido")

def agregar_producto(lista):
    nombre=input("Nombre del producto: ")

    if validar_nombre(nombre)==False:
        print("Error: El nombre no puede estar vacio")
        return

    stock=input("Stock: ")

    if validar_stock(stock)==False:
        print("Error: El stock debe ser un numero entero mayor o igual a 0")
        return

    precio=input("Precio: ")

    if validar_precio(precio)==False:
        print("Error: El precio debe ser un numero mayor que 0")
        return

    producto={
        "nombre": nombre,
        "stock": int(stock),
        "precio": float(precio),
        "disponible": False
    }

    lista.append(producto)
    print("Producto agregado correctamente")

def buscar_producto(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"]==nombre:
            return i
    return -1

def actualizar_disponibilidad(lista):
    for producto in lista:
        if producto["stock"]>0:
            producto["disponible"]=True
        else:
            producto["disponible"]=False

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion==1:
        agregar_producto(productos)

    elif opcion==2:
        nombre=input("Ingrese el nombre del prducto: ")
        lugar=buscar_producto(productos, nombre)

        if lugar!=-1:
            print("Producto encontrado en la posicion", lugar)
            print("Nombre:", productos[lugar]["nombre"])
            print("Stock:", productos[lugar]["stock"])
            print("Precio:", productos[lugar]["precio"])
            print("Disponible:", productos[lugar]["disponible"])
        else:
            print("Producto no encontrado")

    elif opcion==3:
        nombre=input("Ingrese el nombre del producto a eliminar: ")
        lugar=buscar_producto(productos, nombre)

        if lugar!=-1:
            del productos[lugar]
            print("Producto eliminado correctamente")
        else:
            print("El producto", nombre, "no se encuentra registrado")

    elif opcion==4:
        actualizar_disponibilidad(productos)
        print("Disponibilidad actualizada")

    elif opcion==5:
        actualizar_disponibilidad(productos)

        print("===LISTA DE PRODUCTOS===")

        if len(productos)==0:
            print("No hay productos registrados")
        else:
            for producto in productos:
                print("Nombre:", producto["nombre"])
                print("Stock:", producto["stock"])
                print("Precio:", producto["precio"])

                if producto["disponible"]==True:
                    print("Estado: DISPONIBLE")
                else:
                    print("Estado: SIN STOCK")

                print("*"*45)

    elif opcion==6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break