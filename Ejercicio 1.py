#Restriccion: Todos los ejercicios deben resolverse con Python basico. No se permite el uso de librerias externas (NumPy, Pandas, etc.).
#Clean Code: Cada funcion debe tener docstring, nombres en snake_case, codigo legible y modular.

notas = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0, 6.5, 4.3, 5.7, 3.2, 6.1, 4.6]
grados_c = [0, 15, 25, 30, 100]

# 1a) Funciones básicas 
def calcular_suma(datos): 
    suma = 0
    for elemento in datos:
      temporal = elemento
      suma = temporal + suma
    return suma  

def calcular_largo(datos):
    contador = 0
    for elemento in datos:
      contador = contador + 1
    return contador  
 
def calcular_promedio(datos):
   return calcular_suma(datos)/calcular_largo(datos)

def calcular_minimo(datos):
    minimo = 999
    for elemento in datos:
      temporal = elemento
      if minimo > temporal:
          minimo = temporal         
    return minimo  

def calcular_maximo(datos):
    maximo = 0
    for elemento in datos:
      temporal = elemento
      if maximo < temporal:
          maximo = temporal         
    return maximo 

# 1b) Ordenamiento Bubble Sort 
def bubble_sort(datos, orden):
   largo = calcular_largo(datos)
   nueva_lista = datos
   for contador_1 in range(largo):
      for contador_2 in range(largo - 1):
         if orden == 1:
           if nueva_lista[contador_2] > nueva_lista[contador_2 + 1]:
             temporal = nueva_lista[contador_2]
             nueva_lista[contador_2] = nueva_lista[contador_2 + 1]
             nueva_lista[contador_2 + 1] = temporal
         else:
           if nueva_lista[contador_2] < nueva_lista[contador_2 + 1]:
             temporal = nueva_lista[contador_2]
             nueva_lista[contador_2] = nueva_lista[contador_2 + 1]
             nueva_lista[contador_2 + 1] = temporal    
   return nueva_lista        

# 1c) Mediana y Desviación Estándar 
def calcular_mediana(datos):
   lista_ordenada = bubble_sort(datos, 1)
   largo_lista = calcular_largo(lista_ordenada)
   if largo_lista % 2 == 0:
        mediana = (lista_ordenada[int(largo_lista/2) - 1] + lista_ordenada[int(largo_lista/2)]) / 2
   else:
        mediana = (lista_ordenada[int(largo_lista/2)])    
   return mediana
#falta asegurar que entregue un error previsto en caso de que ingresen listas que no sean estrictamente numeros


# 1d) Conversión de Temperaturas
def celcius_a_fahrenheit(grados_c):
   nueva_lista = grados_c
   largo_lista = calcular_largo(grados_c)
   for contador in range(largo_lista):
      nueva_lista[contador] = nueva_lista[contador] * 9/5 + 32
   return nueva_lista  

# 1e) Reporte Estadístico Integrado 
def reporte_estadistico(ciudades):
   for temporal in range(calcular_largo(ciudades)):
      temperaturas = ciudades[temporal]["temperaturas"]
      print("\n\n",ciudades[temporal]["ciudad"])
      print()
      print("Promedio:",calcular_promedio(temperaturas))
      print()
      print("Temperatura maxima:",calcular_maximo(temperaturas))
      print()
      print("Temperatura minima:",calcular_minimo(temperaturas))



orden = int(input("ingresa 1 (ascendentemente) o 0 (descendentemente)"))
print(calcular_suma(notas))
print(calcular_largo(notas))
print(calcular_promedio(notas))
print(calcular_minimo(notas))
print(calcular_maximo(notas))
print(bubble_sort(notas, orden))
print(calcular_mediana(notas))
print(celcius_a_fahrenheit(grados_c))
