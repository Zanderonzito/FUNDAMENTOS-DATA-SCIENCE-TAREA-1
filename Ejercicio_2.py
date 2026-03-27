
#### Tengo la variable student por que me confundia mucho escribiendo estudiante sin S

estudiantes = [
{"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
{"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
{"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},
{"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]},
{"nombre": "Valentina", "notas": [7.0, 6.8, 6.9]},
{"nombre": "Javier", "notas": [4.0, 4.2, 4.1]},
{"nombre": "Camila", "notas": [5.0, 5.5, 5.8]},
{"nombre": "Martín", "notas": [3.5, 4.0, 4.2]},
{"nombre": "Fernanda", "notas": [6.2, 6.5, 6.0]},
{"nombre": "Tomás", "notas": [4.8, 5.0, 5.2]},
{"nombre": "Josefa", "notas": [5.9, 6.0, 6.1]},
{"nombre": "Matías", "notas": [3.8, 4.1, 4.0]},
{"nombre": "Ignacio", "notas": [6.7, 6.9, 7.0]},
{"nombre": "Daniela", "notas": [5.2, 5.4, 5.6]},
{"nombre": "Sebastián", "notas": [4.3, 4.5, 4.7]},
{"nombre": "Gabriela", "notas": [6.0, 6.2, 6.1]},
{"nombre": "Felipe", "notas": [5.7, 5.8, 5.9]},
{"nombre": "Antonia", "notas": [4.9, 5.0, 5.1]},
{"nombre": "Vicente", "notas": [3.7, 4.0, 4.3]},
{"nombre": "Paula", "notas": [6.3, 6.4, 6.5]}]


#Ejercicio 2A

def promedio_estudiante(student):
    
    notas = student["notas"] 
    return sum(notas) / len(notas)

def clasificar_rendimiento(promedio):

    if promedio < 4.0:
        return "Reprovbado"
    elif promedio < 5.0:
        return "Suficiente"
    elif promedio < 6.0:
        return "Aprovado"
    else:
        return "Destacado"


# Retorna lista de dicts: nombre, promedio, estado, nota_max, nota_min, rango.
def generar_reporte(student):
    Reporte = []
    for student in estudiantes:
        notas = student["notas"]
        prom = promedio_estudiante(student)
        estado = clasificar_rendimiento(prom)
        nota_maxima = max(notas)
        nota_minima = min(notas)
        rango_de_notas = nota_maxima - nota_minima
        Reporte.append({
            "nombre": student["nombre"],
            "promedio": round(prom, 2),
            "estado": estado,
            "nota maxima": nota_maxima,
            "nota minima": nota_minima,
            "rango de notas": round(rango_de_notas, 2)
        })
        
    return Reporte




# Ejercicio 2B

def contar_por_estado(reporte):
    conteo = {}
    for estudiante in reporte:
        estado = estudiante["estado"]
        if estado not in conteo:
            conteo[estado] = 0
        conteo[estado] += 1
    return conteo

def filtrar_por_estado(reporte, estado):
    lista = []
    for student in reporte:
        if student["estado"] == estado:
            lista.append(student)
    
    return lista


# Ejercicio 2C



Reporte = generar_reporte(estudiantes)

print("Reporte: ")
for r in Reporte:
    print(r)

print("Conteo por estado: ")
print(contar_por_estado(Reporte))

print("\nSolo aprovados:")
aprovados = filtrar_por_estado(Reporte, "Aprovado")
for student in aprovados:
    print(student)