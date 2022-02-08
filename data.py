# x ejemplo
# / / / / /
# 2
# 5 4 3
# 4 5 6
# / / / / /


n = int(input()) # número de casos (n = 2)
ans = [] # abajo te digo para que es este array
for i in range(n):
    current_data = [int(x) for x in input().split()]
    # cada ciclo for va actualizando los datos
    # (en el primer ciclo, current data va a ser:
    # current_data = [5, 4, 3]
    # en el segundo,
    # current_data = [4, 5, 6])

    # entonces acá escribes el código que necesitas
    # para un solo test case, el for se encargará de aplicarlo 
    # en el resto de casos

    # y por ejemplo, si necesitas cada uno de los valores de
    # current_data puedes hacer:
    a, b, c = current_data[0], current_data[1], current_data[2]

    # (En el primer ciclo,
    # a = 5
    # b = 4
    # c = 3)

    # entonces como ejemplo supongamos que te piden que a cada
    # número de la lista le sumes 1 y en la respuesta pongas
    # cada número separado por un espacio (generalmente es así), 
    # entonces sería:
    for i in current_data:
        i += 1
        ans.append(i) # ans es la lista en donde se irán 
                             # añadiendo las respuestas, porque
                             # por alguna razón si pones print
                             # dentro del ciclo for, las cosas se 
                             # imprimen mal

# y al final solo es poner:
print(*ans) # el asterisco quita los []

# 6 5 4 5 6 7  <-- se imprime eso
