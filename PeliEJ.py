notas=[4.6, 7.0,3.4,6.6 , 3.9, 6.8]

# crear un a funcion para poder pasarle la lista
# como parametro y msotrar el promedio
# mostrar si aprueba o reprueba

def calculaProm(n):
    return round(sum(n)/len(n), 1)
print("El promedio es ", calculaProm(notas))

print(max(notas))
print(min(notas))

peliculas=[
    {"titulo": "Inception", "director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "anio": 2010 },
    {"titulo": "Jurassic Park", "director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "anio": 1993 },
    {"titulo": "Se7en", "director": "David Fincher",
     "genero": "Thiller", "anio": 1997 },

]


# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
#  
'''
1.- ingresar Pelucula
2.- quitar Pelucula
3.- actualizar Pelucula
4.- Mostar Peluculas
5.- Mostrar solo los titulos
6.- Ordenar de mas reciente a mas antigua
7.- Salir
'''




while True:
    print("--- MENU ---")
    print("1.- Ingresar Pelicula")
    print("2.- quitar Pelucula")
    print("3.- actualizar Pelucula")
    print("4.- Mostar Peluculas")
    print("5.- Mostrar solo los titulos")
    print("6.- Ordenar de mas reciente a mas antigua")
    print("7.- Salir")

    opcion=input("Seleccione una opcion: ")

    if opcion=="1":
        titulo=input("Ingrese titulo: ")
        if len(titulo)<=2:
            print("El titulo debe tener mas de 2 caracteres")
        else:
            director=input("Ingrese director (nompre y apellido): ")
            if len(director.split())<2:
                print("Debe ingresar nombre y apellido")
            else:
                genero=input("Ingrese genero: ")
                año=int(input("Ingrese"))

