# Perdidos en la Galaxia

# Nick, Porty y Winter están de viaje por la galaxia en una nave hecha con desperdicios de los estudiantes de MisionTIC. Sin embargo,
# en la basura no había dispositivos para ubicarse en el espacio y ellos se han perdido, lo que ha hecho que Winter se duerma. Nick y 
# Porty deciden pasar el tiempo mientras encuetran algún punto de referencia que los haga retomar un buen camino, y para ello se ponen
# a jugar a ver quien adivin la primera letra del nombre de los planetas que van viendo por el camino, el cual pueden ver a medida que 
# van pasando cerca del mismo. Al ver el nombre del planeta miran si el nombre comienza con una letra que ellos hayan dicho. Si empieza 
# con una de las letras que hayan dicho se les anota un punto, y luego se comparan las puntuaciones. Si Porty lleva más puntos escriben 
# una 'P', si Nick lleva más puntos escriben una 'N', pero si ambos llevan los mismos puntos se anota una 'I'.
# Usted trabaja en una gasolinera espacial en la cual ellos se detinen a tanquear, y le comentan del juego. Debido a usted es 
# programador, decide realizar un programa para este juego de adivinanzas, en donde va a recibir las letras con las que concursa Porty 
# y las letras con las que concursa Nick (ambas como cadena de caracteres), y una cadena de caracteres con las primeras letras de los 
# nombres de los planetas encontrados por Nick y Porty, y debe mostrarse en la consola lo que escribieron Nick y Porty.

# Entrada

# La entrada consta de tres cadenas de caracteres separadas por fin de línea. La primera línea corresponde al grupo de letras de 
# Porty, la segunda línea corresponde al grupo de cuerdas de Nick, y una tercera que corresponde a la secuencia de la primera letra 
# de los nombres de planetas que encuentran Nick y Porty.

# Salida

# Una cadena de caracteres con las letras N, P e I, dependiendo de las puntuaciones que vaya teniendo cada jugador una vez encuentran 
# un planeta.



p = input().upper().strip()
n = input().upper().strip()
planets = input().upper().strip()

def guess_planets(porty, nick, planets):
    score_p = 0
    score_n = 0

    output = ''

    for pos, letter in enumerate(planets):
        #Alguno adivinó el planeta?
        if letter in p:
            score_p += 1
        if letter in n:
            score_n += 1
        # else: pass
            #print('El planeta {} en la posición {} no fue adivinado por ninguno'.format(letter, pos))
        
        #Comparar quién ha adivinado más
        if score_p > score_n:
            output += 'P'
        elif score_p < score_n:
            output += 'N'
        elif score_p == score_n:
            output += 'I'
    
    return output

print(guess_planets(p,n,planets))


