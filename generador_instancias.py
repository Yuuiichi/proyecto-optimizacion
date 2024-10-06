from random import randint as r
from random import shuffle as s

rangos_asignaturas_medianas = ["40-45", "54-58", "68-72", "80-85", "95-99"]
rangos_asignaturas_grandes = ["180-200", "210-230", "250-270", "300-320", "340-360"]

rangos_salas_medianas = ["3", "4", "5", "6", "7"]
rangos_salas_grandes = ["9-11", "12-14", "15-17", "18-20", "21-23"]

def generar_instancias(i):
    i-=1
    archivo = open("instancias.txt", "w")
    archivo.write(">-----------------------------------<\n")

    # Instancias pequeñas
    if i <= 4:
        archivo.write(f"Instancia mediana {i+1}\n")
        rangos_asignaturas_medianas[i] = rangos_asignaturas_medianas[i].split("-")
        rango_inferior = int(rangos_asignaturas_medianas[i][0])
        rango_superior = int(rangos_asignaturas_medianas[i][1])
        cant_asignaturas = r(rango_inferior, rango_superior)
        cant_salas = int(rangos_salas_medianas[i])
        archivo.write(f"Cantidad de asignaturas: {cant_asignaturas}\n")
        archivo.write(f"Cantidad de salas: {cant_salas}\n")

    # Instancias grandes
    else:
        i-=5
        archivo.write(f"Instancia grande {i+1}\n")
        rangos_asignaturas_grandes[i] = rangos_asignaturas_grandes[i].split("-")
        rango_inferior = int(rangos_asignaturas_grandes[i][0])
        rango_superior = int(rangos_asignaturas_grandes[i][1])
        cant_asignaturas = r(rango_inferior, rango_superior)
        archivo.write(f"Cantidad de asignaturas: {cant_asignaturas}\n")
        rangos_salas_grandes[i] = rangos_salas_grandes[i].split("-")
        rango_inferior = int(rangos_salas_grandes[i][0])
        rango_superior = int(rangos_salas_grandes[i][1])
        cant_salas = r(rango_inferior, rango_superior)
        archivo.write(f"Cantidad de salas: {cant_salas}\n")
    
    auxiliar(archivo, cant_asignaturas, cant_salas)
    archivo.close()

    return 0

def auxiliar(archivo, cant_asignaturas, cant_salas):
    
    dosBloques = int(cant_asignaturas * 0.65)
    
    archivo.write(">-----------------------------------<\n")

    for i in range(cant_asignaturas):
        archivo.write(f"Asignatura {i+1}\n")
        archivo.write(f"Prioridad_{i+1}: {r(1, 10)}\n")
        if i < dosBloques:
            archivo.write(f"Cantidad_bloques_{i+1}: 2\n")
        else:
            archivo.write(f"Cantidad_bloques_{i+1}: 1\n")
        archivo.write(f"Alumnos_interesados_{i+1}: {r(10, 40)}\n")
        disponibilidad = []
        for j in range(35):
            cant_disponibilidades = r(14, 28)
            if j < cant_disponibilidades:
                disponibilidad.append(1)
            else:
                disponibilidad.append(0)
        s(disponibilidad)
        archivo.write(f"Disponibilidad_{i+1}: {disponibilidad}\n")
        archivo.write("....................................\n")


    archivo.write(">-----------------------------------<\n")

    for i in range(cant_salas):
        archivo.write(f"Sala {i+1}\n")
        archivo.write(f"Capacidad_{i+1}: {r(20, 45)}\n")
        archivo.write("....................................\n")


i = int(input("Generador de instancias\nIngrese el valor de la instancia posible (1-10): "))
generar_instancias(i)
