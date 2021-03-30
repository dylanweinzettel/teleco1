import csv

with open('espectro.csv') as csvfile:   # Abre el csv
    reader = csv.DictReader(csvfile)    # Devuelve un objeto reader con toda la información del csv como un diccionario
    # Este for es para recorrer cada fila de las que hay en el csv
    for row in reader:
        # Descomenten la siguiente linea si quieren ver la lista de diccionarios
        # print(row)
        pass # Eliminen esta linea cuando empiecen a trabajar
        # TODO