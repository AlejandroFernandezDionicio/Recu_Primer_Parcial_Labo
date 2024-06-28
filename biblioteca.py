import json

def opcion_menu():
    '''Parametros: Ninguno'''
    '''Descripcion: Muestra por terminal las opciones y pide el usuario elegir 1'''
    '''Retorno: Ninguno '''
    print("1-Cargar archivo\n2-Imprimir lista\n3-Asignar totales\n4-Filtrar por tipo\n5-Mostrar servicios\n6-Guardar servicios\n7-Salir")
    opcion = str(input("Opcion: "))
    return opcion

def datos_archivo(nombre_archivo:str):
    '''Recibe como parametro la ubicaciond el archivo
       abre el archivo
       retorna los datos dentro del archivo'''
    try:
        with open(nombre_archivo, "r") as archivo:
            diccionario = json.load(archivo)
            return diccionario
    except FileNotFoundError:
        print(f"{nombre_archivo} no fue encontrado")
        return False

def mostrar_datos(lista:list):
    '''Recibe como parametro una lista
       recorre la lista para mostrar los value de las keys'''
    
    print(f"{"ID_SERVICIO":<42} {"DESCRIPCION":<42} {"TIPO":<42} {"PRECIO_UNITARIO":<42} {"CANTIDAD":<42} {"TOTAL_SERVICIO":<42}")
    for elemento in lista:
        print(f"{elemento["id_servicio"]:<42} {elemento["descripcion"]:<42} {elemento["tipo"]:<42} {elemento["precioUnitario"]:<42} {elemento["cantidad"]:<42} {elemento["totalServicio"]:<42}")

def agrega_totalservicio(lista:list):
    '''Recibe como parametro una lista
       Recorre la lista y en una variable guarda las value de las key asignadas y los castea a float
       con un lambda hace un calculo para tener el total y este mismo se agrega como valor nuevo a la key totalservicio'''
    for elemento in lista:
        cantidad = float(elemento["cantidad"])
        precio = float(elemento["precioUnitario"])
        total = (lambda cantidad,precio: cantidad * precio)(cantidad,precio)
        elemento["totalServicio"] = total

def pedir_nombre():
    '''Pide un nombre al usuario y lo retorna'''
    nombre = input("Ingrese el nombre que tendra el nuevo archivo: ")
    return nombre + ".json"

def pedir_servicio():
    '''No recibe parametros
       pide al usuario una clave en este caso ya declaradas en la variable lista_datos
       donde si el usuario elige una de estas la funcion lo retorna
       sino repite la pregunta'''
    while True:
        lista_servicios = ["Hardware","Software"]
        servicio = input("Ingrese la key que quiera tener el archivo nuevo : ")
        if servicio in lista_servicios:
            return servicio
        else:
            print(f"Error, no se olvide las mayusculas (Sotfware,Hardware)")

def crear_lista(servicio:str,lista:list):
    '''recibe como parametro un servicio y una lista,
    se encarga de appendear en una nueva lista solo elementos que contengan el servicio establecido'''
    lista_nueva = []
    for elementos in lista:
        if elementos["tipo"] == servicio:
            lista_nueva.append(elementos)
    return lista_nueva        


def generar_archivo(nombre_archivo:str,lista:list):
    '''Recibe como parametro la ubicacion del archivo una key y una lista
       abre el archivo en modo de w+ primero escribe el titulo que sera la key
       y recorre la lista para escribir las value de la key en el nuevo archivo generado'''
    try:
        with open(nombre_archivo, "w+") as archivo:
            json.dump(lista, archivo, indent=2)
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
        return False

def ordenamiento(lista:list,clave:str):
    '''Recibe como parametros, una lista y una cadena
       con el metodo sorted y un lambda que me devuelve el contenido de una key
       retorna esta misma como una lista ordenada'''
    lista_ordenada = sorted(lista, key=lambda elemento: elemento[clave])
    return lista_ordenada