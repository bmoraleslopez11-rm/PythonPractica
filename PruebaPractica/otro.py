# # ejemplo de manipulacion de datos en una lista
# listado=[3, 6.5, 4, 5,["Link", "Zelda"], {"pkm":"weeddle"}]
# #        0   1   2  3        4                  5

# print(listado[5]["pkm"])# muestra weeddle, por que es el valor del key "pkm"

# for e in listado:
#     print(e)

# listado.append({"dia": "lunes", "temp": 25.7, "humedad":29})
# print("-"*50)
# input()
# for e in listado:
#     print(e)

# # ejemplo de return

# def suma():
#     return 5+7

# print(suma()*4)

# def calculaIVA(neto):
#     return neto*1.19

# print("El valor a pagar sera:" , calculaIVA(2000))


def verificarNumero():
    while True:
        try:
            num=int(input("Ingrese un numero: "))
            if num<0:
                print("debe ingresar un numero mayor o igual a 0")
            else:
                return num
        except Exception as e:
            print("Solo numero enteros positivos")


pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]

def mostrarPinturas():
    if len(pinturas)<1:
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.- {p}")
            c+=1
def quitarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a eliminar?: "))
    pinturas.pop(ele-1)
def agregarPintura():
    color=input("Que color será?: ")
    capacidad=int(input("Que capacidad será?: "))
    formato=input("Que formato será?: ")
    pinturas.append({"color": color, "capacidad":capacidad, "formato": formato})
def actualizarPintura():
    mostrarPinturas()
    ele=int(input("Que pintura va a actulizar?: "))
    print("1.- Color")
    print("2.- Capacidad")
    print("3.- Formato")
    dato=int(input("Que dato de la pintura va a actulizar?: "))
    nuevoValor=input
    if dato==1:
        nuevoValor=input("Ingrese el nuevo color")
        pinturas[ele-1]["color"]=nuevoValor
    elif dato==2:
        nuevoValor=int(input("Ingrese la nueva capaciadad"))
        pinturas[ele-1]["capacidad"]=nuevoValor
    elif dato==3:
        nuevoValor=input("Ingrese el nuevo formato")
        pinturas[ele-1]["formato"]=nuevoValor
    else:
        print("Dato invalido")
def mayorCap(lista):
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
    return max(listaCapacidad)
def menuPinturas():    
    while True:
        try:
            print("-"*60)
            print("1.- Agregar Pintura")
            print("2.- Quitar Pintura")
            print("3.- Actualizar Pintura")
            print("4.- Mostrar Pinturas")
            print("5.- Mostrar mayor capacidad")
            print("9.- Salir")
            op=int(input("Seleccione una opcion: "))
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
                    print(f"El recipiente con mayor capacidad tine : {mayorCap(pinturas)}")           
                case 9:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion invalida")
        except Exception as e:
            print("error: ", e)
    
menuPinturas()




