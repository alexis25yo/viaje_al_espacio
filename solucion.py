# Importar las librerias necesarias
import pandas as pd

def linea_separacion():
    print( '**'.center (80,'*'))

# Declaración de variables. Se crean listas vacías que corresponden a los atributos de las naves
Tipo_de_nave = []
Pais = []
Nombre_nave = []
Año_primer_lanzamiento = []

# Se muestra en pantalla el menú de bienvenida.
linea_separacion()
print('ESTE ES EL PROGRAMA DE REGISTRO DE NAVES'. center (80,'*'))
linea_separacion()
nombre = str(input('Por favor ingrese su nombre: '))
nombre = nombre.upper()

# Se crea un cliclo para que el programa se ejecute de manera infinita, hasta que el usuario decida finalizarlo.
while True:
    # Creacion menú principal. En este apartado se solita al usuario seleccional la acción que requiera.
    linea_separacion()
    print('Login:', nombre)
    print('¿Qué deseas hacer?'. center (80))
    print("""                                                   
          (1) Agregar nueva nave                                    
          (2) Filtrar 
          (3) Ver todas las naves 
          (4) Descargar base de datos actual
          (5) Información general de la base de datos
          (6) Salir 
          """. center(80)) 
    res = input('Ingrese el número correspondiente a la opción requerida: ')
    linea_separacion()
    # Con la función Try se encapsula un posible error cuando el usuario ingrese una opción no descrita en el menú
    try:
        respuesta = int(res)
        # Creación de función condicional para la selección de las opciones del menú principal        
        # Opción 1. (Agregar nueva nave). El programa llega a esta opción cuando el usuario selecciona 1.
        # Se le pide al usuario que ingrese las caracteristicas de la nave que desea crea y se almacena en diferentes variables
        if respuesta == 1: 
            atn = input('Ingrese el tipo de nave: ')                  
            ap = input('Ingrese el pais: ')                           
            ann = input('Ingrese el nombre de la nave: ')                
            apl = input('Ingrese año del primer lanzamiento: ')
            
            # Las variables que contienen las caracteristicas de las naves se almacenan en las listas vacías creadas previamente. 
            Tipo_de_nave.append(atn)                                
            Pais.append(ap)
            Nombre_nave.append(ann)                                           
            Año_primer_lanzamiento.append(apl)
                
            # Se crea un DataFrame con las listas que incluyen las caracteristicas de las naves creadas.
            df = pd.DataFrame(list(zip(Tipo_de_nave, Pais, Nombre_nave, Año_primer_lanzamiento)),
            columns = ['Tipo de nave', 'Pais', 'Nombre de la nave', 'Año del primer lanzamiento'])
            
            # Se exporta el DataFrame a un archivo .xlsx
            df = df.to_excel('naves_espaciales.xlsx', )
            
            
                               
        # Opción 2. (Filtrar). El programa llega a esta opción cuando el usuario selecciona 2.   
        # Se le pide al usuario que ingrese la opción correspondiente al atributo por el cual desea filtrar
        elif respuesta == 2:            
            print("""
            (a) Tipo nave 
            (b) Pais
            (c) Nombre  de la nave
            (d) Año del primer lanzamiento
              """)            
            atributo = str(input('Ingrese el número del atributo que desea buscar: '))
                     
            # Al ingresar la opción 'a' el programa realiza el filtro en la ... 
            #columna del tipo de nave, según el dato ingresado por el usuario. 
            if atributo == 'a':              
                filtrar = input('Ingrese el tipo de nave que desea filtrar: ')
                df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)
                df3 = df2[df2['Tipo de nave'] == filtrar]
                linea_separacion()
                print(df3)
                linea_separacion()
                # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                print("""
                ¿Desea descargar la base de datos filtrada?
                (a) Si, deseo descargarla.
                (b) No gracias.
                """)
                respuesta = str(input('Ingrese una opción:'))
                if respuesta == 'a':
                    df3.to_excel('filtro_por_tipo_de_nave.xlsx')
                    linea_separacion()
                    print('...Base de datos descargada satisactoriamente... '. center (80,'*'))
                else:
                    continue              
              
                
            # Al ingresar la opción 'b' el programa realiza el filtro en la ... 
            #columna del pais, según el dato ingresado por el usuario. 
            elif atributo == 'b':
                filtrar = input('Ingrese el pais que desea filtrar: ')
                df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)
                df3 = df2[df2['Pais'] == filtrar]
                linea_separacion()
                print(df3)
                linea_separacion()
                # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                print("""
                ¿Desea descargar la base de datos filtrada?
                (a) Si, deseo descargarla.
                (b) No gracias.
                """)
                respuesta = str(input('Ingrese una opción:'))
                if respuesta == 'a':
                    df3.to_excel('Filtro_por_pais.xlsx')
                    linea_separacion()
                    print('...Base de datos descargada satisfactoriamente... '. center (80,'*'))
                else:
                    continue
                
            # Al ingresar la opción 'c' el programa realiza el filtro en la ... 
            #columna del nombre de la nave, según el dato ingresado por el usuario.    
            elif atributo == 'c':
                filtrar = input('Ingrese el nombre de la nave que desea filtrar: ')
                df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)
                df3 = df2[df2['Nombre de la nave'] == filtrar]
                linea_separacion()
                print(df3)
                linea_separacion()
                # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                print("""
                ¿Desea descargar la base de datos filtrada?
                (a) Si, deseo descargarla.
                (b) No gracias.
                """)
                respuesta = str(input('Ingrese una opción:'))
                if respuesta == 'a':
                    df3.to_excel('Filtro_por_nombre_de_nave.xlsx')
                    linea_separacion()
                    print('...Base de datos descargada satisfactoriamente... '. center (80,'*'))
                else:
                    continue
               
            # Al ingresar la opción 'd' el programa realiza el filtro en la ... 
            #columna del año del primer lanzamiento, con valores iguales al año ingresado                
            elif atributo == 'd':
                #En este menú, se solicita al ususario ingresar la letra correspondiente al tipo de filtro requerido
                print("""
                Seleccione el filtro que desea aplicar.
                
                (a) Filtrar por naves lanzadas en el año:
                (b) Filtrar por naves lanzadas despues del año:
                (c) Filtrar por naves lanzadas antes del año:
                """)
                filtrar = str(input('Ingrese la opción deseada: '))
                
                # Al ingresar la opción 'a' el programa realiza el filtro en la ... 
                #columna del año del primer lanzamiento, con valores iguales al año ingresado
                if filtrar == 'a':
                    df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)                    
                    filtro = int(input('Ingrese el año que desea filtrar: '))
                    df3 = df2[df2['Año del primer lanzamiento'] == filtro]
                    linea_separacion()
                    print(df3)
                    linea_separacion()
                    # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                    print("""
                    ¿Desea descargar la base de datos filtrada?
                    (a) Si, deseo descargarla.
                    (b) No gracias.
                    """)
                    respuesta = str(input('Ingrese una opción:'))
                    if respuesta == 'a':
                        df3.to_excel('Filtro_por_año_de_lanzamiento.xlsx')
                        linea_separacion()
                        print('...Base de datos descargada satisactoriamente... '. center (80,'*'))               
                
                # Al ingresar la opción 'b' el programa realiza el filtro en la ... 
                #columna del año del primer lanzamiento, con valores superiores al año ingresado
                elif filtrar == 'b':
                    df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)                    
                    filtro = int(input('Ingrese el año que desea filtrar: '))
                    df3 = df2[df2['Año del primer lanzamiento']  > filtro]
                    df3 = df3.sort_values(by = ['Año del primer lanzamiento'], ascending = [True])
                    linea_separacion()
                    print(df3)
                    linea_separacion()
                    # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                    print("""
                    ¿Desea descargar la base de datos filtrada?
                    (a) Si, deseo descargarla.
                    (b) No gracias.
                    """)
                    respuesta = str(input('Ingrese una opción:'))
                    if respuesta == 'a':
                        df3.to_excel('Filtro_por_años_posteriores.xlsx')
                        linea_separacion()
                        print('...Base de datos descargada satisactoriamente... '. center (80,'*'))
                
                # Al ingresar la opción 'c' el programa realiza el filtro en la ... 
                #columna del año del primer lanzamiento, con valores inferiores al año ingresado
                elif filtrar == 'c':
                    df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)                    
                    filtro = int(input('Ingrese el año que desea filtrar: '))
                    df3 = df2[df2['Año del primer lanzamiento']  < filtro]
                    df3 = df3.sort_values(by = ['Año del primer lanzamiento'], ascending = [False])
                    linea_separacion()
                    print(df3)
                    linea_separacion()
                    # Se le solicita al usuario ingresar una opción en caso de que desee descargar el DataFrame en un archivo .xlsx
                    print("""
                    ¿Desea descargar la base de datos filtrada?
                    (a) Si, deseo descargarla.
                    (b) No gracias.
                    """)
                    respuesta = str(input('Ingrese una opción:'))
                    # Al ingresar la opción 'a' el programa guarda el DataFrame en formato .xlsx
                    if respuesta == 'a':
                        df3.to_excel('Filtro_por_años_anteriores.xlsx')
                        linea_separacion()
                        print('...Base de datos descargada satisactoriamente... '. center (80,'*'))
                else:
                    continue
                
                    
           
        # Opción 3. (Ver todas las naves). El programa llega a esta opción cuando el usuario selecciona 3.
        # Se muestra en pantalla el DataFrame que incluye todos los registros de las naves ingresadas.
        elif respuesta == 3:
            print('Registros actuales'. center (80,'*'))
            print('**'.center (80,'*'))
            df2 = pd.read_excel('naves_espaciales.xlsx', index_col = 0)
            print(df2)
        
        # Opción 4. (Descargar base de datos actual). El programa llega a esta opción cuando el usuario selecciona 4.
        # El prorama descarga en un archivo .xlsx el DataFrame que incluye todos los registros de las naves ingresadas.        
        elif respuesta == 4:
            df = pd.DataFrame(list(zip(Tipo_de_nave, Pais, Nombre_nave, Año_primer_lanzamiento)),
                columns = ['Tipo de nave', 'Pais', 'Nombre de la nave', 'Año del primer lanzamiento'])
           
            df.to_excel('naves_espaciales.xlsx')
            print('Inventario de naves descargado satisfactoriamente '. center (80,'*'))
                  
       
        # Opción 5. (Información general de la base de datos). El programa llega a esta opción cuando el usuario selecciona 5.
        # El programa muestra en pantalla la información general del DataFrame.   
        elif respuesta == 5:
           df.info()
           
        # Opción 6. (Salir del programa). El programa llega a esta opción cuando el usuario selecciona 6.
        # El programa se cierra.   
        elif respuesta == 6:
            break
        
        # Se captura el error originado por el tipo de variable ingresado por el usiario en el menu principal.
    except:        
        print('Error. Por favor ingrese una opción válida (numeros enteros del 1 al 6)')
        salida = input('presione enter para continuar')
        continue
               
    else:
        continue
