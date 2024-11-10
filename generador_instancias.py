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
    
    # Se crea el archivo instancias.dzn
    archivo = open(str("instancia_{}_{}.dzn".format(cant_asignaturas, cant_salas)), "w")

    auxiliar(archivo, cant_asignaturas, cant_salas)
    archivo.close()

    return 0

def auxiliar(archivo, cant_asignaturas, cant_salas):
    
    # Se crea una lista de las asignaturas indispensables
    indispensables = []
    for i in range(cant_asignaturas):
        if (i + 1) % 5 == 0:            # Cada 5 asignaturas se asigna una como indispensable
            indispensables.append("true")
        else:
            indispensables.append("false")    # 0 en caso de que la asignatura no sea indispensable
    s(indispensables)

    # Calcula la cantidad de asignaturas que tendrán 1 bloque (65% de las asignaturas por B = 1)
    unBloque = int(cant_asignaturas * 0.65)
    bloques = [1] * unBloque + [2] * (cant_asignaturas - unBloque)
    s(bloques)
    
    # Se escriben las variables en el archivo
    for i in range(cant_asignaturas):

        # Se indica si la asignatura es indispensable
        archivo.write(f"% Parametros de Asignatura {i+1}\nindispensabilidad_asignatura_{i+1} = {indispensables[i]};\n")

        # Se asigna una prioridad a la asignatura
        if indispensables[i] == 1:
            archivo.write(f"prioridad_asignatura_{i+1} = {r(6,10)};\n") # En caso de que sea indispensable
        else:
            archivo.write(f"prioridad_asignatura_{i+1} = {r(1,5)};\n")  # En caso de que no sea indispensable
        
        # Se asigna la cantidad de bloques a la asignatura
        archivo.write(f"bloques_asignatura_{i+1} = {bloques[i]};\n")
        
        # Se asigna una cantidad de alumnos interesados a la asignatura basados en nuestro valor de A (A = 1)
        archivo.write(f"alumnos_interesados_asignatura_{i+1} = {r(10, 40)};\n")
        
        # Se asigna una cantidad de horas a la asignatura basados la disponibilidad de los profesores
        disponibilidad = []
        for _ in range(5):
            if bloques[i] == 2:
                # Ensure two 'true's are next to each other
                row = ["false"] * 7
                start = r(0, 5)
                row[start] = "true"
                row[start + 1] = "true"
            else:
                # Ensure there is a separation
                row = ["false"] * 7
                true_positions = [0, 2, 4, 6]
                s(true_positions)
                row[true_positions[0]] = "true"
            disponibilidad.append(row)
        archivo.write(f"asignatura_{i+1}_disponibilidad = [|\n")
        for j in disponibilidad:
            if disponibilidad.index(j) + 1 == len(disponibilidad):
                archivo.write(f"    {', '.join(j)}|];\n\n")
            else:
                archivo.write(f"    {', '.join(j)}|\n")

    archivo.write("% Parametros capacidad de salas\n")
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
