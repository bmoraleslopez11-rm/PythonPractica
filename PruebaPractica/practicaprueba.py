
def suma(a, b):
    print(a+b)

suma(22, 363)

notas1=[6.3,6.8, 3.7, 2.1]
notas2=[6.3,1.8, 3.9, 2.1]

def creaProm(n):
   return round(sum(n)/len(n),1)


print("El promedio del notas 1 es", creaProm(notas1))
print("El promedio del notas 2 es", creaProm(notas2))


# Cree una funcion para buscar un color especifico
# Pase la lista como argumento, y el color
# como segundo argumento. Rerotne "Disponible"
# Si el color existe. "No exite" en caso contrario

def verificarNumero():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if num < 0:
                print("Debe ingresar un numero mayor o igual a 0")
            else:
                return num
        except Exception as e:
            print("Solo numeros enteros positivos")


pinturas = [
    {"color": "verde", "capacidad": 1500, "formato": "tarro"},
    {"color": "azul", "capacidad": 1500, "formato": "tarro"},
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"},
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"},
]


def mostrarPinturas():
    if len(pinturas)<1:
        print("No hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.-{p}")
            c+=1


def quitarPintura():
    mostrarPinturas()
    ele = int(input("¿Qué pintura va a eliminar?: "))
    pinturas.pop(ele - 1)


def agregarPintura():
    color = input("¿Qué color será?: ")
    capacidad = int(input("¿Qué capacidad será?: "))
    formato = input("¿Qué formato será?: ")
    pinturas.append({
        "color": color,
        "capacidad": capacidad,
        "formato": formato
    })


def actualizarPintura():
    mostrarPinturas()
    ele = int(input("¿Qué pintura va a actualizar?: "))

    print("1.- Color")
    print("2.- Capacidad")
    print("3.- Formato")

    dato = int(input("¿Qué dato de la pintura va a actualizar?: "))

    if dato == 1:
        nuevoValor = input("Ingrese el nuevo color: ")
        pinturas[ele - 1]["color"] = nuevoValor

    elif dato == 2:
        nuevoValor = int(input("Ingrese la nueva capacidad: "))
        pinturas[ele - 1]["capacidad"] = nuevoValor

    elif dato == 3:
        nuevoValor = input("Ingrese el nuevo formato: ")
        pinturas[ele - 1]["formato"] = nuevoValor

    else:
        print("Dato inválido")


def mayorCap(lista):
    listaCapacidad = []

    for p in lista:
        listaCapacidad.append(p["capacidad"])

    return max(listaCapacidad)



def buscarColor(lista, color):
    for pintura in lista:
        if pintura["color"].lower() == color.lower():
            return "Disponible"
    return "No existe"


def menuPinturas():
    while True:
        try:
            print("-" * 60)
            print("1.- Agregar Pintura")
            print("2.- Quitar Pintura")
            print("3.- Actualizar Pintura")
            print("4.- Mostrar Pinturas")
            print("5.- Mostrar mayor capacidad")
            print("6.- Buscar color")
            print("9.- Salir")

            op = int(input("Seleccione una opcion: "))

            match op:
                case 1:
                    agregarPintura()

                case 2:
                    quitarPintura()

                case 3:
                    actualizarPintura()

                case 4:
                    mostrarPinturas()

                case 5:
                    print(
                        f"El recipiente con mayor capacidad tiene: {mayorCap(pinturas)}"
                    )

                case 6:
                    colorBuscar = input("Ingrese el color a buscar: ")
                    print(buscarColor(pinturas, colorBuscar))

                case 9:
                    print("Saliendo...")
                    break

                case _:
                    print("Opción inválida")

        except Exception as e:
            print("Error:", e)


menuPinturas()