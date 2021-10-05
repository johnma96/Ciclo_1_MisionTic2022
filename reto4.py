# Nick y Porty: El Segundo Contacto
# Nick y Porty deciden tomar una aventura más allá de los bordes conocidos del universo, siguiendo los caminos de la nave Community la cual se perdió al sobrepasar dichos bordes. En este camino, Nick y Porty encuentran un primer planeta, que suena muy interesante, y con los radares de última tecnología que tienen en la nave encuentran que la Community dejó una bitácora de su exploración en dicho planeta.

# Siguiendo las leyes de la exploración espacial, se debe respetar la ley del primer contacto: jamás afectar la civilización que nunca ha conocido vida de otros mundos; sin embargo, este es el segundo contacto, y Nick tiene ganas de afectar la civilización. Porty, con su tradicional temor, lo convence de que no es lo apropiado, y que mejor exploren el planeta. Así, logran encontrar una caverna con algunos mensajes pictográficos interesantes del origen de dicha civilización, y se dan cuenta que en la bitácora existe un capítulo de los avances de los tripulantes de la Community para interpretar estos mensajes y convertirlos a un idioma interpretable para los terrícolas.

# Así, en la bitácora existe un tipo de diccionario que hace equilavencia de algunos 
# símbolos contra letras del alfabeto conocido por Nick y Porty. Nick y Porty toman 
# fotografías de los mensajes, se llevan la bitácora y regresan al sistema solar, en 
# donde usted ya ha cerrado su etapa como chef de parada, y ahora vende café en la 
# librería "El ABC de Veth". 

# Ellos se enteran de esto, y recuerdan sus contribuciones en el pasado y deciden ir a 
# buscarlo para realice un programa que de forma automática lea símbolos basados en las
# fotografías de los mensajes pictográficos, revise cuáles de esos se encuentra en el 
# capítulo de la bitácora, y escriba un mensaje con la interpretación de los símbolos y 
# la secuencia de símbolos que pudieron ser interpretados.

# El proceso que han definido usted, Nick y Porty, es el siguiente: el programa va a 
# recibir un diccionario de traducción en el cuál estará el símbolo del planeta 
# inexplorado y su correspondiente traducción según la bitácora; de igual manera, 
# se ingresará la sucesión de símbolos observados en una fotografía, los cuales no se 
# repiten por imagen. Es importante recalcar que no todos los símbolos en la imagen 
# tendrán una traducción en el diccionario. En este orden de ideas, usted generará dos 
# salidas: la primera es la traducción obtenida con los símbolos que se pudieron 
# interpretar, y además de esto generara una lista con los símbolos que se pudieron 
# interpretar.

# Entrada

# La primera línea será una cadena de caracteres que contendrá un diccionario, cuyas 
# claves serán cadenas de caracteres y sus valores también serán cadenas de caracteres, 
# que contiene la información del símbolo del planeta inexplorado como clave y su 
# equivalente a alfabeto terrícola como valor. La segunda línea es la secuencia de 
# símbolos del mensaje del planeta inexplorado, separados por coma.

# Ejm: 

# "{"&": "y", "#": "t", "\": "h", "$": "p", "(": "n", "?": "h", "@": "d", "<": "o"}"

# "=,>,$,%,&,[,],),#,:,?,;,<,(,|"

# Salida

# La primera línea será una cadena de caracteres con los símbolos traducidos sin ningún 
# tipo de separación. La segunda línea será una cadena de caracteres que contendrá los 
# símbolos que fueron traducidos, separados por un espacio.

# "python"
# "$ & # ? < ("


# import json

# dic_str = input()
# sequence = input()

# dic_traslate = json.loads(dic_str)

# lst_traslate = []
# lst_symbols_traslates = []

# for symbol in sequence.split(','):
#     if symbol in dic_traslate.keys():
#         traslate = dic_traslate[symbol]
#         lst_traslate.append(traslate)
#         lst_symbols_traslates.append(symbol)
#     else:
#         pass

# print(''.join(lst_traslate))
# print(' '.join(lst_symbols_traslates))   

entrada = '{"&": "y", "#": "t", "\": "h", "$": "p", "(": "n", "?": "h", "@": "d", "<": "o"}'

clave_valor = entrada.split(",")
print(clave_valor)
diction = {elem.split(':')[0] : elem.split(':')[1] for elem in clave_valor}
print(diction)
print(type(diction))