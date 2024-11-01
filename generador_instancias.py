from random import randint as r
from random import shuffle as s

# Definimos los rangos de las instancias medianas y grandes según nuestro B asignado (B = 1).
rangos_asignaturas_medianas = ["40-45", "54-58", "68-72", "80-85", "95-99"]
rangos_asignaturas_grandes = ["180-200", "210-230", "250-270", "300-320", "340-360"]

rangos_salas_medianas = ["3", "4", "5", "6", "7"]
rangos_salas_grandes = ["9-11", "12-14", "15-17", "18-20", "21-23"]

def generar_instancias(i):
    # Se resta 1 para que el índice sea correcto
    i-=1

    # Se crea el archivo instancias.dzn
    archivo = open("instancias.dzn", "w")

    # Código para instancias medianas
    if i <= 4:
        rangos_asignaturas_medianas[i] = rangos_asignaturas_medianas[i].split("-")  # Se separa el rango en dos números
        rango_inferior = int(rangos_asignaturas_medianas[i][0])                     # Se obtiene el rango inferior
        rango_superior = int(rangos_asignaturas_medianas[i][1])                     # Se obtiene el rango superior
        cant_asignaturas = r(rango_inferior, rango_superior)                        # Se obtiene la cantidad de asignaturas usando random
        cant_salas = int(rangos_salas_medianas[i])                                  # Se obtiene la cantidad de salas

    # Código para instancias grandes
    else:
        i-=5
        rangos_asignaturas_grandes[i] = rangos_asignaturas_grandes[i].split("-")    # Se separa el rango en dos números
        rango_inferior = int(rangos_asignaturas_grandes[i][0])                      # Se obtiene el rango inferior
        rango_superior = int(rangos_asignaturas_grandes[i][1])                      # Se obtiene el rango superior
        cant_asignaturas = r(rango_inferior, rango_superior)                        # Se obtiene la cantidad de asignaturas usando random
        
        rangos_salas_grandes[i] = rangos_salas_grandes[i].split("-")                # Se separa el rango en dos números
        rango_inferior = int(rangos_salas_grandes[i][0])                            # Se obtiene el rango inferior
        rango_superior = int(rangos_salas_grandes[i][1])                            # Se obtiene el rango superior
        cant_salas = r(rango_inferior, rango_superior)                              # Se obtiene la cantidad de salas usando random
    
    auxiliar(archivo, cant_asignaturas, cant_salas)
    archivo.close()

    return 0

def auxiliar(archivo, cant_asignaturas, cant_salas):
    
    # Calcula la cantidad de asignaturas que tendrán 2 bloques (65% de las asignaturas)
    dosBloques = int(cant_asignaturas * 0.65)
    
    # Se escriben las variables en el archivo
    for i in range(cant_asignaturas):
        archivo.write(f"asignatura_prioridad_{i+1} = {r(1, 10)};\n")                # Se asigna una prioridad a la asignatura
        
        # Se asigna la cantidad de bloques a la asignatura
        if i < dosBloques:
            archivo.write(f"asignatura_{i+1}_cantidad_bloques = 2;\n")              # 65% de las asignaturas tendrán 2 bloques
        else:
            archivo.write(f"asignatura_{i+1}_cantidad_bloques = 1;\n")              # 35% de las asignaturas tendrán 1 bloque
        
        # Se asigna una cantidad de alumnos interesados a la asignatura basados en nuestro valor de A (A = 1)
        archivo.write(f"alumnos_interesados_asignatura_{i+1} = {r(10, 40)};\n")
        
        # Se asigna una cantidad de horas a la asignatura basados la disponibilidad de los profesores
        disponibilidad = []
        for j in range(35):
            cant_disponibilidades = r(14, 28)   # Se asigna una cantidad de disponibilidades a cada profesor (Se explica en el informe)
            if j < cant_disponibilidades:
                disponibilidad.append(1)        # 1 en caso de que el profesor esté disponible
            else:
                disponibilidad.append(0)        # 0 en caso de que el profesor no esté disponible
        s(disponibilidad)
        archivo.write(f"asignatura_{i+1}_disponibilidad = {disponibilidad};\n")

    for i in range(cant_salas):
        # Se asigna una capacidad a la sala basados en nuestro valor de A (A = 1)
        archivo.write(f"capacidad_sala_{i+1} = {r(20, 45)};\n")


print("         Cant.asignaturas    Cant.salas")
print("1:             40-45             3")
print("2:             54-58             4")
print("3:             68-72             5")
print("4:             80-85             6")
print("5:             95-99             7")
print("6:            180-200           9-11")
print("7:            210-230          12-14")
print("8:            250-270          15-17")
print("9:            300-320          18-20")
print("10:           340-360          21-23")
instancia = int(input("Ingrese el valor de la instancia posible (1-10): "))
generar_instancias(instancia)
