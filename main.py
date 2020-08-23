# 17:'00

print("PROGRAMA DE CALCULO DE NOTAS DE 3 ALUMNOS")
print()
print("Ingresar 5 notas por alumno e imprimir la nota promedio, el menor y el mayor.")

alumno1 = {
    "nombre" :"Charly",
    "apellido" : "Chinchay",
    "notas" : [],
    "nota_promedio" : 0,
    "nota_menor" : 0,
    "nota_mayor" : 0
}

alumno2 = {
    "nombre" :"Marvin",
    "apellido" : "Chinchay",
    "notas" : [],
    "nota_promedio" : 0,
    "nota_menor" : 0,
    "nota_mayor" : 0
}
alumno3 = {
    "nombre" : "Grecia",
    "apellido" : "Ayala",
    "notas" : [],
    "nota_promedio" : 0,
    "nota_menor" : 0,
    "nota_mayor" : 0
}

alumnos = {}
alumnos["alumno1"] = alumno1
alumnos["alumno2"] = alumno2
alumnos["alumno3"] = alumno3

numero_nota = 1
no_es_nota = True
nota = -1

try:
    for x, y in alumnos.items():

        alumno = y
        nota_alumno = alumno["notas"]
        nombre_alumno = alumno["nombre"]
        numero_nota = 1

        print()
        print(f"Ingrese notas para el alumno {nombre_alumno}.")

        while True:
            no_es_nota = True

            while no_es_nota:
                try:
                    print(f"Ingrese nota {numero_nota}:", end="")
                    nota = int(input())
                    no_es_nota = False
                except Exception:
                    print(f"[Error_tipo_dato]: Ingresar número entero, sin decimales.")
                else:
                    if nota < 0 or nota > 20:
                        print(f"[Error_nota]: Valor de nota corresponde valores entre 0 y 20.")
                        no_es_nota = True

            nota_alumno.append(nota)
            
            if numero_nota == 5:
                alumno["nota_promedio"] = round(sum(nota_alumno) / numero_nota)
                alumno["nota_menor"] = min(nota_alumno)
                alumno["nota_mayor"] = max(nota_alumno)
                break

            numero_nota = numero_nota + 1

    print("------------------------------------------")
    for x, y in alumnos.items():
        nombre = y["nombre"]
        apellido = y["apellido"]
        nota_promedio = y["nota_promedio"]
        nota_menor = y["nota_menor"]
        nota_mayor = y["nota_mayor"]

        print(f"Notas del alumno {nombre} {apellido}")
        print()
        print(f"Nota promedio: {nota_promedio}")
        print(f"Nota menor: {nota_menor}")
        print(f"Nota mayor: {nota_mayor}")
        print()

except KeyboardInterrupt:
    print("[Error_usuario]: Programa cancelado por el usuario")