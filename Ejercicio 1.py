#Restriccion: Todos los ejercicios deben resolverse con Python basico. No se permite el uso de librerias externas (NumPy, Pandas, etc.).
#Clean Code: Cada funcion debe tener docstring, nombres en snake_case, codigo legible y modular.

notas = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0, 6.5, 4.3, 5.7, 3.2, 6.1, 4.6]

def calcular_suma(datos): 
    suma = 0
    for elemento in notas:
      temporal = elemento
      suma = temporal + suma
    return suma  

def calcular_largo(notas):
    contador = 0
    for elemento in notas:
      contador = contador + 1
    return contador  
 
def calcular_promedio(notas):
   return calcular_suma(notas)/calcular_largo(notas)

def calcular_minimo(notas):
    minimo = 999
    for elemento in notas:
      temporal = elemento
      if minimo > temporal:
          minimo = temporal         
    return minimo  

def calcular_maximo(notas):
    maximo = 0
    for elemento in notas:
      temporal = elemento
      if maximo < temporal:
          maximo = temporal         
    return maximo 

def bubble_sort(notas, orden):
   largo = calcular_largo(notas)
   nueva_lista = notas
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

def calcular_mediana(notas):
   lista_ordenada = bubble_sort(notas, 1)
   largo_lista = calcular_largo(lista_ordenada)
   if largo_lista % 2 == 0:
        mediana = (lista_ordenada[int(largo_lista/2) - 1] + lista_ordenada[int(largo_lista/2)]) / 2
   else:
        mediana = (lista_ordenada[int(largo_lista/2)])    
   return mediana
#falta asegurar que entregue un error previsto en caso de que ingresen listas que no sean estrictamente numeros

orden = int(input("ingresa 1 (ascendentemente) o 0 (descendentemente)"))
print(calcular_suma(notas))
print(calcular_largo(notas))
print(calcular_promedio(notas))
print(calcular_minimo(notas))
print(calcular_maximo(notas))
print(bubble_sort(notas, orden))
print(calcular_mediana(notas))