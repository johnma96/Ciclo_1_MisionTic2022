# Nick y Porty: El Perreo Intenso Cósmico

# Porty se ha enterado que los tripulantes de la nave mis_tic_cic_1_p39 están terminando su viaje. Por ello, 
# Porty decide armar una fiesta llamada "el perreo intenso cósmico", en dónde estarán cantando grandes artistas, 
# incluyendo al Abuelo Melquiades. Morty ha construido una lista inicial de las personas que van a asistir a 
# la fiesta; sin embargo, Nick se entera y decide invitar amigos también a esta fiesta, la cual se realizará 
# en un planeta afuera de la tierra, y allí viene un problema y es el concepto de alienígena: hay que recordar 
# que los terrícolas fuera de la tierra son considerados alienígenas. Como es de esperar, esto va a generar 
# problemas y diferencias entre Nick y Porty, además de confusiones porque algunos de los alienígenas 
# (incluyendo terrícolas) son amigos en común, así que pueden aparecer en ambas listas.

# Usted los está escuchando discutir, y se da cuenta que desde ya puede adivinar algunos de los problemas que 
# van a pasar, y que fijo lo van a poner a programar una solución para eso; anticipándose, decide crear un 
# módulo de Python propio para que cuando sea el momento, usted invoque soluciones que ya ha definido, y con 
# eso, además de resolverles el problema, no se aguanta la intensidad de los locos esos. Ya llegaron los 
# invitados, y están formados en una fila, por el mismo desorden de información a cada uno se le asigno un 
# turno en orden de llegara (la primera persona que llega tiene el primer turno). Usted ha decidido llamar a 
# la librería 'perreo_cosmico' [1 punto], y le debe colocar las siguientes funciones:

# 1) [1 punto] Función 'tipo_alienigenas' que va a recibir una lista, la cual se obtiene de una columna de 
# la lista de invitados que determina el tipo de alienígena. Para facilitar el ingreso, se deben determinar 
# los tipos de alienígenas existentes, así que la función debe retornar los tipos de alienígenas sin repetir 
# que aparecen en dicha lista.

# Por ejemplo. si la lista original es:

# tipo_alienigenas(['jupetarienses', 'terrícolas', 'jupetarienses', 'mercurianos', 'terrícolas', 'terrícolas'])

# La función debería retornar:

# ['mercurianos', 'terrícolas', 'mercurianos']

# 2) [1 punto] Función 'si_son', la cual va a recibir algunos turnos de la fila de asistentes, una lista con 
# el tipo de alienígena de cada uno de los alienígenas en la fila (en el mismo orden de llegada, es decir, el 
# primer tipo de la lista corresponde al primer alienígena en la fila), y un tipo de alienígena a verificar en 
# los turnos definidos, esto porque entre tanta gente, se confunde un poco el invitado a qué área se debe 
# dirigir, y también es complicado confiar del todo en la palabra de cada uno: todos quieren ver el show de 
# la forma más relajada posible. Así que la función va a retornar una lista con los turnos de los invitados 
# que efectivamente tienen el tipo de alienígena que se está verificando.

# Por ejemplo, si los parámetros son:

# si_son([1,3,5,7], ['jupetarienses', 'terrícolas', 'jupetarienses', 'mercurianos', 'terrícolas', 'terrícolas', 'mercurianos', 'jupetarienses'], 'jupetarienses')

# La función debería retornar

# [1,3]

# 3) [1 punto] La función 'no_estan', la cual va a recibir dos listas: los turnos en la fila de los invitados en 
# la lista de Nick, y los turnos en la fila de los invitados por Porty, y debe determinar cuales de los invitados 
# de Nick no han sido invitados por Porty (para evitar confusiones, y también evitar colados). 

# Por ejemplo, a la siguiente entrada:

# no_estan([1,2,3,5,7,8], [2,3,7,8])

# La salida debería ser:

# [1,5]

# 4) [1 punto] La función 'uno_y_uno', que va a recibir la lista de Nick y la lista de Porty. Esta función surge 
# por un motivo, se está llenando el lugar del evento, y Porty ha discutido con Nick de quién debería entrar. Han 
# logrado llegar al acuerdo de que de los invitados que no están en ambas listas, va a entrar uno y uno de cada 
# lista. La función debe retornar la cantidad de alienígenas de cada lista que podrían entrar al evento.

# Por ejemplo, a la siguiente entrada:

# uno_y_uno([1,2,4,5,7,8], [2,3,7,8])

# La salida debería ser:

# 1

# porque de la lista de Porty (segunda lista) solo el alienígena en el turno 3 es válido para ingresar, y así un 
# invitado de la lista de Nick, en este caso el alienígena del turno 1, podría ingresar como corresponde.

# Entrada:

# Este programa no requiere entrada. Ni generará salida. Se requiere que el estudiante genere un archivo con el 
# nombre perreo_intenso.py y que se respeten los nombres de las funciones dadas y sus parámetros.

# NOTAS: LA PRIMERA FUNCIÓN EN REALIDAD DEBIÓ LLAMARSE tipo_melenudos PARA PASAR EL AUTOGRADER. LAS VERIFICACIONES EN
# LAS FUNCIONES tipo_melenudos y no_estan DEBEN HACERSE EN ORDEN PARA QUE PASAR, RAZÓN POR LA QUE FUNCIONES COMO
# set DE PYTHON NO PUDIERON SER EMPLEADAS. LOS TURNOS DADOS EN LA FUNCIÓN si_son COINCIDE CON LA INDEXACIÓN QUE HACE 
# PYTHON EN LAS LISTAS, POR EJEMPLO, SI PIDEN VERIFICAR EL TURNO 4, SE REFIEREN A LA POSICIÓN 4 DE LA LISTA COMENZANDO
# A CONTAR DESDE EL 0

def tipo_melenudos(lst_tipo_alienigena):
    unicos = []
    for alienigena in lst_tipo_alienigena:
        if not(alienigena in unicos): unicos.append(alienigena)   
    return unicos

def si_son(turnos, lst_tipo_alienigena, tipo_alie_verif):
    alienigenas_verificados = [turno for turno in turnos if lst_tipo_alienigena[turno] == tipo_alie_verif]
    return alienigenas_verificados

def no_estan(invitados_nick, invitados_porty):
    en_nick_no_porty = [invitado for invitado in invitados_nick if not(invitado in invitados_porty)]
    return (en_nick_no_porty)

def uno_y_uno(invitados_nick, invitados_porty):
    no_estan_nick, no_estan_porty = no_estan(invitados_nick, invitados_porty), no_estan(invitados_porty, invitados_nick)
    if len(no_estan_nick) < len(no_estan_porty): return len(no_estan_nick)
    else: return len(no_estan_porty)