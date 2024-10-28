def gestionador():
    print('Bienvenido al gestionador de clientes, cual de las siguientes opciones desea realizar:\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar ')

    CONTINUE = False

    lista_clientes = []

    while not CONTINUE:

        while True:
            try:
                opcion = int(input('Ingrese un numero de opcion'))
                if opcion in list(range(1,7)):
                    break
                else:
                    print('Ingrese un numero válido')
            except Exception as e:
                print('Ingrese uno de los numeros válidos')



        # Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos
        if opcion == 1:

            nombre_cliente = input('Ingrese el nombre de cliente a agregar: ')   

            while True:
                try:
                    nif_cliente = int(input('Ingrese el NIF del cliente (numero), sin puntos ni guion: '))   #defino variable nif en un bucle para q ingrese un integer
                    break
                except Exception as e:
                    print('Ingrese un numero válido de NIF')

            direccion_cliente = input(f'ingrese una direccion del cliente: {nombre_cliente}')

            while True:
                try:
                    telefono_cliente = int(input(f'ingrese el telefono del cliente {nombre_cliente}'))
                    break
                except Exception as e:
                    print(f'Ingresa un numero válido de telefono del cliente {nombre_cliente}, sin puntos, guiones, cimbolos ni letras')

            correo_cliente = input(f'Ingresa el correo de {nombre_cliente}')

            while True:
                try:
                    cliente_preferente = input(f'Es "{nombre_cliente}" un cliente preferente? (si/no)')
                    if cliente_preferente.lower() == 'si':
                        cliente_preferente = True
                        break
                    elif cliente_preferente.lower() == 'no':
                        cliente_preferente = False
                        break
                    else:
                        print(f'Ingresa "si" si {nombre_cliente} es cliente preferente, en caso contrario ingresa "no"')

                except Exception as e:
                    print(f'Ingresa "si" si {nombre_cliente} es cliente preferente, en caso contrario ingresa "no"')


            diccionario_cliente = {nif_cliente: {'nombre_cliente': nombre_cliente,
                                                 'direccion': direccion_cliente,
                                                 'telefono': telefono_cliente,
                                                 'correo': correo_cliente,
                                                 'preferente': cliente_preferente}}
            
            lista_clientes.append(diccionario_cliente)
            


        # Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
        elif opcion == 2:
            while True:
                if lista_clientes == []:
                    print('No hay clientes registrados para eliminar')
                    break
                else:
                    #Preguntar por nif del cliente
                    while True:
                        try:
                            nif_cliente = int(input('Ingrese el NIF del cliente (numero), sin puntos ni guion que desea eliminar: '))   #defino variable nif en un bucle para q ingrese un integer

                            encontrado = False
   
                            for diccionario in lista_clientes:      #itero por cada diccionario de clientes en lista_clientes
                                for key in diccionario.keys():
                                    print(f"Verificando cliente con NIF: {key}")
                                    if int(key) == nif_cliente:       #si el nif ingresado esta presente en la clave. el int garantiza que se compare con INT
                                        lista_clientes.remove(diccionario)      #de la lista clientes elimino el diccionario
                                        print(f'Se ha eliminado correctamente el usuario con NIF {nif_cliente}')
                                        encontrado = True
                                        break   #salimos del bucle despues de eliminar
                            
                            if encontrado:
                                break          # AL UTILIZAR ESTA VARIABLE BANDERA NOS ASEGURAMOS SALIR SUTILMENTE DEL BUCLE SIN PASAR POR EL PRINT SIGUIENTE

                            print(f'No se encontró el NIF {nif_cliente}')
                                
                            break

                        except Exception as e:
                            print('Ingrese un numero existente de nif')
                
                break

                                    

        # Preguntar por el NIF del cliente y mostrar sus datos.
        elif opcion == 3:
            while True:
                if lista_clientes == []:
                    print('No hay clientes registrados para ver')
                    break
                else:
                    #Preguntar por nif del cliente
                    while True:
                        try:
                            nif_cliente = int(input('Ingrese el nif del cliente para obtener sus datos: '))

                            encontrado = False

                            for diccionario in lista_clientes:
                                for key in diccionario.keys():
                                    if int(key) == nif_cliente:
                                        print(f'Los datos del cliente {diccionario[key]['nombre_cliente']} son: \n '
                                            f'Nombre: {diccionario[key]['nombre_cliente']}\n '
                                            f'Direccion: {diccionario[key]['direccion']}\n '
                                            f'Telefono: {diccionario[key]['telefono']}\n '
                                            f'Correo: {diccionario[key]['correo']}\n '
                                            f'Preferente: {diccionario[key]['preferente']}')
                                        encontrado = True
                                        break
                            
                            if encontrado:
                                break       #SALIMOS SUTILMENTE DEL BUCLE CON LA VARIABLE BANDERA

                            print('No se encontró el numero NIF ingresado')
                            break
                        except Exception as e:
                            print('Ingrese un numero de nif valido')

                    break



        # Mostrar lista de todos los clientes de la base datos con su NIF y nombre
        elif opcion == 4:
            print('Lista de clientes: ')
            for diccionario in lista_clientes:
                for key, value in diccionario.items():
                    print([f'Nombre: {value['nombre_cliente']}', f'NIF: {key}'])



        # Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
        elif opcion == 5:
            print('Clientes Preferentes: ')
            for diccionario in lista_clientes:
                for key, value in diccionario.items():
                    if value['preferente']:
                        print('Lista de clientes preferentes: \n'
                            f'Nombre: {value['nombre_cliente']}    Nif: {key} ')



        # Salir del programa
        else:
            CONTINUE = True



    print(lista_clientes)


    for diccionario in lista_clientes:
        for key, value in diccionario.items():
            print(f'NIF del cliente: {key}')
            print(f'Nombre del cliente: {value['nombre_cliente']}\nDireccion: {value['direccion']}\nTelefono: {value['telefono']}\nCorreo: {value['correo']}\nEs preferente?: {value['preferente']}')

    
if __name__=='__main__':
    gestionador()