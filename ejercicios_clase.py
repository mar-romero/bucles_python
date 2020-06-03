#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios con bucles "while"

    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    val_max = 6
    while x <= val_max:    # reemplace "condicion" por lo que crea necesario
        if x == val_max:
            print('x=', x, 'se termina el programa')
            break
        x += 1
    
        # Coloque la línea de código para que "X" incremente "1"

    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    val_max1 = 0
    while x >= val_max1:    # reemplace "condicion" por lo que crea necesario
        if x <= val_max1:
            print("Valor de x =", x)
            break
        x -= 1

        
        # Coloque la línea de código para que "X" decremente "1"


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = [ 'rojo', 'naranja', 'verde', 'azul' ]
    
    for x in colores :
        if (x == 'rojo') :
            print (x)
        if (x == 'naranja'):
            print (x)
        if (x == 'verde'):
            print (x)
        if (x == 'azul'):
            print (x)
        
    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...
    # No lo entiendo

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...
    
    col_len = len (colores)
    
    for i in range(col_len) :
        if i == 0:
            col = colores[i]
            print(col)
        if i == 1:
            col = colores[i]
            print(col)
        if i == 2:
            col = colores[i]
            print(col)
        if i == 3:
            col = colores[i]
            print(col)

def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero

    for x in numeros:
        suma += x
        print("número = ", x , "sumatoria =", suma)

def ej4():
    # Ejercicios con bucles "while"

    x = 0
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    while x < 10 and x !=6:
        print(x)
        x += 2
        print(x)

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    y = 0
    while y < 10 :
        if y == 6:
            print('Es igual a 6')
            break
        print(y)
        y += 2
        print(y)

def ej5():
    # Ejercicio de seuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    # fin....
    fin = int(input('Ingrese el ultimo numero de la secuencia\n'))

    lista = []
    suma = 0
    
    for x in range(inicio, fin + 1):
        suma += x
    print('suma', suma)

    
    # for ... in range(....)

    

    

    # Imprimir el valor de la sumatoria


def ej6():
    # Ejercicio de seuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    # fin....
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))
    
    lista = []
    lista_a = []
    cantidad_numeros_positivos = 0  # Inicializo el contador en 0
    #cantidad_numeros_negativos
    for x in range (inicio, fin + 1):
        if x >= 0:
            lista.append(x)
    print('la cantidad de numeros positivos son:', len(lista))
    for y in range (inicio, fin + 1):
        if y < 0:
            lista_a.append(y)
    print('la cantidad de numeros negativos son:', len(lista_a))


    # for ... in range(....)

    # Imprimir el valor de la cantidad de números positivos y negativos
    #NO PUDE HACERLO CON CANTIDAD DE NUMEROS POSITIVOS += 1 LO HICE AGREGANDO EL NUMERO A UNA LISTA
    #Y DESPUES CONTAR LA CANTIDAD DE LA LISTA

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    ej6()
