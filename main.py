from biblioteca import*
carga_datos = False
opcion_5 = False
while True:
    opcion = opcion_menu()
    if opcion == "1":
       lista = datos_archivo("compu.json")
       carga_datos = True
    elif opcion == "2":
        if carga_datos == True:
            mostrar_datos(lista)
        else:
            print("PRIMERO ACCEDA A LA OPCION 1")
    elif opcion == "3":
        if carga_datos == True:
            agrega_totalservicio(lista)
            print("TOTALSERVICIO AGREGADO CON EXITO")
        else:
            print("PRIMERO ACCEDA A LA OPCION 1")
    elif opcion == "4":
        if carga_datos == True:
            nombre_archivo = pedir_nombre()
            servicio = pedir_servicio()
            nueva_lista = crear_lista(servicio,lista)
            generar_archivo(nombre_archivo,nueva_lista)
        else:
            print("PRIMERO ACCEDA A LA OPCION 1")
    elif opcion == "5":
        if carga_datos == True:
            lista_ordenada = ordenamiento(lista,"descripcion")
            opcion_5 = True
        else:
            print("PRIMERO ACCEDA A LA OPCION 1")
    elif opcion == "6":
        if opcion_5 == True and carga_datos == True:
            nombre_archivo = pedir_nombre()
            generar_archivo(nombre_archivo,lista_ordenada)
        else:
            print("PRIMERO ACCEDA A LA OPCION 1/5")
    elif opcion == "7":
        break