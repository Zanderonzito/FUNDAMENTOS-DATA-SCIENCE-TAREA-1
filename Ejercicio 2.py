#Tenemos la variable student por que a uno de nuestros compañeros le complicó mucho escribir estudiante sin S
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
    {"nombre": "Paula", "notas": [6.3, 6.4, 6.5]}
]

#|||||||||||||||EJERCICIO 2A||||||||||||||||||||||
def promedio_estudiante(student):
    "Aquí calculamos y retornamos el promedio de un estudiante"
    notas = student["notas"] 
    return sum(notas) / len(notas)

def clasificar_rendimiento(promedio):
    "Aquí más que todo clasificamos el promedio según los rangos establecidos"
    if promedio < 4.0:
        return "Reprobado"
    elif promedio < 5.0:
        return "Suficiente"
    elif promedio < 6.0:
        return "Aprobado"
    else:
        return "Destacado"

def generar_reporte(lista_estudiantes):
    "Aquí retornamos la lista de dicts: nombre, promedio, estado, nota_max, nota_min, rango."
    Reporte = []
    for student in lista_estudiantes:
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
    
#||||||||||||||||EJERCICIO 2B|||||||||||||||||||||
def contar_por_estado(reporte):
    "Aquí más que todo está la dict con la cantidad de alumnos por cada estado."
    conteo = {}
    for student in reporte:
        estado = student["estado"]
        if estado not in conteo:
            conteo[estado] = 0
        conteo[estado] += 1
    return conteo

def filtrar_por_estado(reporte, estado):
    "Aquí retornamos una lista filtrada de estudiantes según el estado dado."
    lista = []
    for student in reporte:
        if student["estado"] == estado:
            lista.append(student)
    return lista

#|||||||||||||||||||||||EJERCICIO 2C|||||||||||||||||||||
def ordenar_reporte(reporte, clave='promedio', descendente=True):
    "Aquí ordenamos en si, cualquier clave numérica usando bubble sort."
    registro = list(reporte)
    numero = len(registro)
    for iteracion in range(numero):
        for posicion in range(0, numero - iteracion - 1):
            if descendente:
                if registro[posicion][clave] < registro[posicion + 1][clave]:
                    registro[posicion], registro[posicion + 1] = registro[posicion + 1], registro[posicion]
            else:
                if registro[posicion][clave] > registro[posicion + 1][clave]:
                    registro[posicion], registro[posicion + 1] = registro[posicion + 1], registro[posicion]
    return registro

#||||||||||||||||||||||||Ejercicio 2D|||||||||||||||||||||
def buscar_estudiante(lista_estudiantes, nombre):
    "Aquí hicimos la función para buscar estudiantes."
    for student in lista_estudiantes:
        if student["nombre"].lower() == nombre.lower():
            return student
    return None

def buscar_por_rango_promedio(reporte, minimo, maximo):
    "Aquí más que todo filtramos los estudiantes cuyo promedio esté entre el mínimo y máximo dados."
    lista = []
    for student in reporte:
        if minimo <= student["promedio"] <= maximo:
            lista.append(student)
    return lista


if __name__ == "__main__":
    #Aquí generamos el reporte base usando la función del 2A, de esa manera no hacemos más funciones
    Reporte = generar_reporte(estudiantes)
    
    #||||||||||||||||||||||||| MENÚ PARA EL SISTEMA |||||||||||||||||||
    while True:
        print("\n" + "="*55)
        print("     SISTEMA DE CLASIFICACIÓN ACADÉMICA DE UTEM")
        print("="*55)
        print("1. Mostrar reporte completo (2A")
        print("2. Mostrar conteo por estado (2B)")
        print("3. Mostrar listado de Aprobados (2B)")
        print("4. Mostrar Ranking por Promedio (2C)") 
        print("5. Buscar estudiante por nombre (2D)")
        print("6. Mostrar análisis de consistencia (2E)")
        print("7. Salir")
        print("-" * 55)
        
        opcion = input("Ingrese número de la opción que desea: ")
        print("") 
        
        if opcion == "1":
            print("==> REPORTE COMPLETO:")
            for r in Reporte:
                print(f"Nombre: {r['nombre']} | Promedio: {r['promedio']} ({r['estado']}) | Rango: {r['rango de notas']}")
                

        elif opcion == "2":
            print("===> CONTEO POR ESTADO:")
            conteo_estados = contar_por_estado(Reporte)
            for estado, cantidad in conteo_estados.items():
                print(f" - {estado}: {cantidad} alumnos")
                

        elif opcion == "3":
            print("===> ESTUDIANTES APROBADOS:")
            aprobados = filtrar_por_estado(Reporte, "Aprobado")
            if len(aprobados) == 0:
                print("No hay estudiantes con estado Aprobado.")
            else:
                for student in aprobados:
                    print(f" - {student['nombre']} (Promedio: {student['promedio']})")
                    

        elif opcion == "4":
            print("===> RANKING DE ESTUDIANTES (Del mejor a peor):")
            reporte_ordenado = ordenar_reporte(Reporte, clave='promedio', descendente=True)
            for i, r in enumerate(reporte_ordenado):
                print(f" {i+1}. {r['nombre']} - Promedio: {r['promedio']}")
                

        elif opcion == "5":
            nombre_buscado = input("Estimado, porfavor, ingrese el nombre del estudiante a buscar: ")
            encontrado = buscar_estudiante(Reporte, nombre_buscado)
            
            if encontrado:
                print("\n===> ESTUDIANTE ENCONTRADO:")
                print(f"Nombre: {encontrado['nombre']} | Promedio: {encontrado['promedio']} ({encontrado['estado']})")
            else:
                print("\nEl estudiante no se encuentra en los registros.")
                

        elif opcion == "6":
            print("===> ANÁLISIS DE CONSISTENCIA:")
            mas_consistente = Reporte[0]
            mas_inconsistente = Reporte[0]
            
            for student in Reporte:
                if student["rango de notas"] < mas_consistente["rango de notas"]:
                    mas_consistente = student
                if student["rango de notas"] > mas_inconsistente["rango de notas"]:
                    mas_inconsistente = student
                    
            print(f"  - Más consistente: {mas_consistente['nombre']} (Rango: {mas_consistente['rango de notas']})")
            print(f"  - Más inconsistente: {mas_inconsistente['nombre']} (Rango: {mas_inconsistente['rango de notas']})")
            
            
        elif opcion == "7":
            
            print("Nos vemos!! saludosss!!!")
            break 
            

        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 7.")