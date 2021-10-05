# Nick y Porty: La Aguapanela Oscura Concentrada

# Nick y Porty siguen en sus aventuras por la galaxia. Esta vez, Perry se ha colado en la nabe, lo que avergüenza a Porty. Como 
# Perry está aburrido, y no entiende mucho de lo que pasa, decide ayudarle a Nick con una tarea muy simple: crear combustible de 
# alta velocidad para la nave.

# Este combustible se llama “La Aguapanela Oscura Concentrada”, debido a la gran cantidad de energía que le provee a la nave. 
# Nick está probando distintas fórmulas, y Perry debe ayudarle a organizarlas de forma consecutiva para que sea exactamente lo 
# que se necesita. Así, Nick y Porty empiezan a enlistar las partículas que necesitan para generar “La Aguapanela Oscura Concentrada”,
# y la tarea de Perry es escribir estos valores, separados por guión, y determinar de manera consecutiva qué y cuántas partículas 
# se necesitan de cada tipo. Las partículas están determinadas por símbolos alienígenas asociados a elementos desconocidos en la 
# tierra: #, $, %, !, ?, ;, *, +, ¬.

# En ejemplo de esto sería el siguiente, luego de que Nick y Porty comienzan a nombrar partículas de elementos y Perry escribe 
# en primera instancia: #-#-#-!-!-?-+-¬-¬-!-#. Así, Perry determina que el siguiente es el orden de partículas necesario: 
# # (3 unidades), ! (2 unidades), ? (1 unidad), + (1 unidad), ¬ (2 unidades), ! (1 unidad), y # (1 unidad). 
# Luego de entender esa respuesta, para facilitar la lectura, Perry decide utilizar el siguiente formato (primera línea el 
# nombre del elemento, y la segunda línea la cantidad de partículas de dicho elemento según el orden):

# # ! ? + ¬ ! #

# 3 2 1 1 2 1 1

# Sin embargo, Perry está haciendo todo esto de manera manual. Ellos paran en su restaurante “Python Parado Espacial” a comer algo, 
# y usted nota la lentitud con la cual Perry hace esta tarea; para evitar las burlas de Nick y la pena de Porty, usted decide ayudar 
# a Perry con un programa que facilita la tarea luego de escribir la primera sucesión de partículas alienigenas. Desarrolle un 
# programa en python que reciba como entrada el listado de las partículas separadas por guión que arma Perry, y genera la salida 
# en formato bonito del orden de partículas (una partícula puede aparece más de una vez en la salida pero no de forma consecutiva) 
# junto con otra línea que corresponde a la cantidad de partículas consecutivas del elemento alienigena.

# Entrada
# Cadena de caracteres que corresponde a la sucesión de partículas alienígenas separadas por coma.

# Ejm: ?-*-*-#-+-+-+-#-?-%-+-¬

#Salida

# Dos cadenas de caracteres: la primera, con la secuencia organizada de elementos alienígenas a utilizar; la segunda, con la 
# cantidad de partículas de cada elemento a utilizar de acuerdo al orden establecido por Nick y Porty.

# ejm : 
# ? * # + # ? % + ¬

# 1 2 1 3 1 1 1 1 1

formula_aguapanela = input()
lst_formula = formula_aguapanela.split('-')

elemento = [lst_formula[0]]
cantidad = [0]

actual_pos = 0

for index_elemento in range(0,len(lst_formula)):
    if lst_formula[index_elemento] == elemento[actual_pos]:
        cantidad[actual_pos] = cantidad[actual_pos] + 1
    else:
        actual_pos += 1
        elemento.append(lst_formula[index_elemento])
        cantidad.append(1)

print(' '.join(elemento))
print(' '.join([str(i) for i in cantidad]))





