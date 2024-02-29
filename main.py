from models import (Ejercicio, 
                    Cardio,
                    Fuerza,
                    Cliente,
                    Crossfitero,
                    Culturista,
                    Ciclista,
                    Entrenador)


# nuevo_ejerc = Cardio("correr", 3, 120, 260)
# crofi = Crossfitero("carlo", "21/21/2000", 90, 3, 2, 1)
# crofi.agregar_ejercicio(nuevo_ejerc)


# lista = []

# contador_fuerza = 0
# contador_cardio = 0
# for elemento in lista:
#     if type(elemento) == Fuerza():
#         contador_fuerza += 1
#     else:
#         contador_cardio += 1

# ejercicios = [...]  # Tu lista de ejercicios

# ejercicios_filtrados = [
#     ejercicio for ejercicio in ejercicios 
#     if abs(ejercicios.count('fuerza') - ejercicios.count('cardio')) in [-1, 0, 1]
# ]

# check = lambda x, y : x - y in [-1, 0, 1]

repetir = True
cliente_seleccionado = None
entrenador_seleccionado = None
lista_ejercicios = []
lista_clientes = []
lista_entrenadores = []



def modificar_ejercicio(lista_ejercicios):
    ejercicio_a_modificar = input("Introduzca el ejercicio que quiera modificar: ")
    for elemento in lista_ejercicios:
        if ejercicio_a_modificar.lower() == elemento.nombre:
            if type(elemento) == Fuerza:
                print("Introduzca los nuevos valores: ")
                elemento.nombre = input("Introduzca nuevo nombre del ejercicio de fuerza: ")
                elemento.nivel_de_dificultad = int(input("Introduzca nuevo nivel de dificultad del ejercicio: "))
                elemento.calorias = int(input("Introduzca las nuevas calorias consumidas por ese ejercicio en una hora: "))
                elemento.series = int(input("Introduzca el nuevo numero de series: "))
                elemento.repeticiones = int(input("Introduzca el nuevo numero de repeticiones: "))
                elemento.tiempo_tension = int(input("Introduzca el tiempo en tension: "))
                elemento.tiempo_descanso = int(input("Introduzca el tiempo de descanso: "))
                return f"Ejercicio actualizado correctamente: {elemento}"
            elif type(elemento) == Cardio:
                print("Introduzca los nuevos valores: ")
                elemento.nombre = input("Introduzca nuevo nombre del ejercicio de cardio: ")
                elemento.nivel_de_dificultad = int(input("Introduzca nuevo nivel de dificultad del ejercicio: "))
                elemento.calorias = int(input("Introduzca las nuevas calorias consumidas por ese ejercicio en una hora: "))
                elemento.duracion = int(input("Nuevo tiempo que debe durar ese ejercicio (en horas): "))
                return f"Ejercicio actualizado correctamente: {elemento}"
            else:
                return "Opcion no valida"






while repetir:
    print("\nA- Ejercicios \nB- Clientes \nC- Entrenadores\nD- Salir")
    opcion = (input("¿Que desea hacer?: "))
    if opcion.lower() == "a":
        print("\nA- Crear ejercicio \nB- Consultar ejercicios \nC- Borrar ejercicio")
        opcion_1 = (input("¿Que desea hacer?: "))
        if opcion_1.lower() == "a":
            opcion_1_1 = input("¿Quieres crear un ejercicio de fuerza o de cardio?: ")
            if opcion_1_1.lower() == "cardio":
                nombre_ej_cardio = input("Introduzca nombre del ejercicio de cardio: ")
                nvl_dificultad = int(input("Introduzca nivel de dificultad del ejercicio: "))
                calorias = int(input("Introduzca calorias consumidas por ese ejercicio en una hora: "))
                duracion = int(input("Tiempo que debe durar ese ejercicio (en horas): "))
                lista_ejercicios.append(Cardio(nombre_ej_cardio, nvl_dificultad, calorias, duracion))
        
            elif opcion_1_1.lower() == "fuerza":
                nombre_ej_fuerza = input("Introduzca nombre del ejercicio de fuerza: ")
                nvl_dificultad = int(input("Introduzca nivel de dificultad del ejercicio: "))
                calorias = int(input("Introduzca calorias consumidas por ese ejercicio en una hora: "))
                series = int(input("Introduzca numero de series: "))
                repeticiones = int(input("Introduzca numero de repeticiones: "))
                tiempo_tension = int(input("Introduzca tiempo en tension: "))
                tiempo_descanso = int(input("Introduzca tiempo de descanso: "))
                lista_ejercicios.append(Fuerza(nombre_ej_fuerza, nvl_dificultad, calorias, series, repeticiones, tiempo_tension, tiempo_descanso))
            else:
                print("Opcion no valida")

        elif opcion_1.lower() == "b":
            print("Visualizar ejercicios")
            if not lista_ejercicios:
                print("Debe crear al menos 1 ejercicio")
            else:
                for ejercicio in lista_ejercicios:
                    print(ejercicio)
                modificar = input("¿Quiere modificar algun ejercicio? (s/n): ")
                if modificar.lower() == "s":
                    modificar_ejercicio(lista_ejercicios)

                

        elif opcion_1.lower() == "c":
            ejercicio_borrar = input("Introduzca que ejercicio desea borrar: ")
            for elemento in lista_ejercicios:
                if elemento.lower() == ejercicio_borrar:
                    lista_ejercicios.remove(elemento)
                    print("Ejercicio borrado correctamente.")






    elif opcion.lower() == "b":
        print("\nA- Crear cliente \nB- Consultar clientes \nC- Calcular ejercicio \nD- Modificar cliente \nE- Borrar cliente \nF- Cliente seleccionado ")
        opcion_2 = input("¿Que desea hacer?: ")

        if opcion_2.lower() == "a":

            print("Creación de un cliente")
            nombre_cliente = input("Introduzca nombre del cliente: ")
            fecha_nac = input("Introduzca fecha de nacimiento: ")
            peso_cliente = int(input("Introduzca peso del cliente: "))
            cond_fisica = int(input("Introduzca condicion fisica del cliente: "))
            lista_clientes.append(Cliente(nombre_cliente, fecha_nac,peso_cliente,cond_fisica))
            nuevo_cliente = Cliente(nombre_cliente, fecha_nac,peso_cliente,cond_fisica)
            print(nuevo_cliente)
            print("Ahora asignale uno o mas ejercicios: ")
            if not lista_ejercicios:
                print("Debe crear al menos 1 ejercicio")
            else:
                for ejercicio in lista_ejercicios:
                    print(ejercicio)
                asignacion_ejercicio = input("¿Que ejercicio desea asignarle al nuevo cliente?: ")
                for ejercicio in lista_ejercicios:
                    if asignacion_ejercicio.lower() == ejercicio.nombre:
                        nuevo_cliente.asignar_entrenamiento(ejercicio)
                        

        elif opcion_2.lower() == "b":
            if not lista_clientes:
                print("Crea al menos 1 cliente para consultar los clientes.")
            else:
                for cliente in lista_clientes:
                    print(cliente)
                seleccion = input("Seleccione un cliente: ")
                for cliente in lista_clientes:
                    if seleccion.lower() == cliente.nombre:
                        cliente_seleccionado = cliente
                        
                print(f"Cliente seleccionado: {cliente_seleccionado.nombre}")

        elif opcion_2.lower() == "c":
            if not cliente_seleccionado:
                print("Debe crear y/o seleccionar un cliente")
            else:
                seleccion.calcular_entrenamiento()

        elif opcion_2.lower() == "d":
            if not cliente_seleccionado: 
                print("Ningun cliente seleccionado. Cree o seleccione uno")
            else:
                print(f"Modificando cliente : {cliente_seleccionado.nombre}")
                cliente_seleccionado.nombre = input("Introduzca nuevo nombre del cliente: ")
                cliente_seleccionado.fecha_nacimiento = input("Introduzca nueva fecha de nacimiento del cliente: ")
                cliente_seleccionado.peso = input("Introduzca nuevo peso del cliente: ")
                cliente_seleccionado.condicion_fisica = input("Introduzca nueva condicion fisica: ")
                print(cliente_seleccionado)

        elif opcion_2.lower() == "e":
            if not cliente_seleccionado:
                print("Ningun cliente seleccionado. Cree o seleccione uno")
            else:
                lista_clientes.remove(cliente_seleccionado)

        elif opcion_2.lower() == "f":
            if not cliente_seleccionado:
                print("Ningun cliente seleccionado. Cree o seleccione uno")
            else:
                print(cliente_seleccionado)


    elif opcion.lower() == "c":
        print("\nA- Crear entrenador \nB- Consultar entrenadores \nC- Ver lista de clientes del entrenador \nD- Modificar el entrenador \nE- Borrar entrenador\nF- Entrenador selecionado")
        opcion_3 = input("¿Que desea hacer?: ")
        if opcion_3.lower() == "a":
            print("Creacion de un entrenador: ")
            nombre_entrenador = input("Introduzca nombre del entrenador: ")
            nuevo_entrenador = Entrenador(nombre_entrenador)
            lista_entrenadores.append(nuevo_entrenador)
            print("Asignale un cliente")
            if not lista_clientes:
                print("Debe crear un cliente para poder asignarle uno")
            else:
                for cliente in lista_clientes:
                    print(cliente)
                asignacion_cliente = input("Que cliente quiere asignarle a este entrenador: ")
                for cliente in lista_clientes:
                    if asignacion_cliente.lower() == cliente.nombre:
                        nuevo_entrenador.asignar_cliente(cliente)
                    
                
                
                

        elif opcion_3.lower() == "b":
            if not lista_entrenadores:
                print("Debe crear al menos 1 entrenador para consultar los entrenadores")
            else:
                for entrenador in lista_entrenadores:
                    print(entrenador)
                seleccion2 = input("Seleccione un entrenador: ")

                for entrenador in lista_entrenadores:
                    if seleccion2.lower() == entrenador.nombre:
                        entrenador_seleccionado = entrenador
                print(f"Entrenador seleccionado: {entrenador_seleccionado.nombre}")


        elif opcion_3.lower() == "c":
            if not lista_entrenadores:
                print("Debe crear al menos 1 entrenador para consultar los clientes de este")
            elif entrenador_seleccionado is None:
                print("Primero seleccione un entrenador.")
            else:
                entrenador_seleccionado.consultar_clientes()


        elif opcion_3.lower() == "d":
            if not lista_entrenadores:
                print("Debe crear al menos 1 entrenador para modificarlo")
            elif entrenador_seleccionado is None:
                print("Primero seleccione un entrenador.")
            else:
                entrenador_seleccionado.nombre = input("Introduzca nuevo nombre del entrenador: ")


        elif opcion_3.lower() == "e":
            if not lista_entrenadores:
                print("Debe crear al menos 1 entrenador para borrarlo")
            elif entrenador_seleccionado is None:
                print("Primero seleccione un entrenador.")
            else:
                if entrenador_seleccionado in lista_entrenadores:
                    print(f"Entrenador '{entrenador_seleccionado.nombre}' borrado")
                    lista_entrenadores.remove(entrenador_seleccionado)
                    entrenador_seleccionado = None


        elif opcion_3.lower() == "f":
            if entrenador_seleccionado is not None:
                print(entrenador_seleccionado)
            else:
                print("Ninguno")








    elif opcion.lower() == "d":
        print("Hasta la proxima")
        repetir = False




    else:
        print("opcion no valida!")























