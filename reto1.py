# Reforma Tributaria

# La nueva reforma tributaria plantea categorizar el estatus tributario de las 
# personas a partir de la cantidad de dinero que paguen de impuestos (valores 
# enteros), de acuerdo con los siguientes criterios:

# - Una persona está en categoría 1 si paga entre $0 y $20. 

# - Una persona está en categoría 2 si paga entre $21 y $30.

# - Una persona está en categoría 3 si paga entre $31 y $50. 

# - Una persona está en categoría 4 si paga más de $50. 

# Cuando fueron Álvaro, Betty y Camilo a pagar los impuestos al banco. Álvaro, 
# se percató que a lo que él pago le hicieron falta $4 para ser tres (3) veces lo 
# que pagó Betty, y que lo que él pagó junto con lo que pago Betty, fue 5 veces lo 
# que pagó Camilo.

# Entrada

# La entrada es un número entero que representa la cantidad de dinero que pagó Betty

# Salida

# Tres enteros separados por espacio que representan los valores que pagaron Betty,
# Álvaro y Camilo respectivamente, separados por un sólo espacio (sólo números, 
# sin el símbolo $) y en la segunda línea indique en que categoría tributaria (el 
# número escrito en letras minúsculas) en la cual quedó clasificado Camilo.

# Ejemplo

# Entrada: 19

# Salida: 

# 19 42 12
# uno

def pagos():
    betty = int(input())
    alvaro = int((3 * betty) - 4)
    camilo = int((alvaro + betty)/5)
    return betty, alvaro, camilo

def categorias_tributarias(persona):
    if persona >= 0 and persona <= 20:
        categoria = 'uno'
    elif persona >= 21 and persona <= 30:
        categoria = 'dos'
    elif persona >= 31 and persona <= 50:
        categoria = 'tres'
    elif persona > 50:
        categoria = 'cuatro'
    else:
        categoria = 'Sin categoria'
    return categoria

def main():
    categoria_camilo = categorias_tributarias(camilo)
    return categoria_camilo

betty, alvaro, camilo = pagos()
print(betty, alvaro, camilo, sep = ' ')
print(main())