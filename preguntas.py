"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    Suma_col_dos = 0
    
    with open('data.csv', 'r') as f:        
        for fila in f:
            fila = fila.split('\t')
            Suma_col_dos = Suma_col_dos + float(fila[1])
    return Suma_col_dos


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    with open('data.csv','r') as f:
        f = [lista.replace('\n','') for lista in f]
        f = [sep.split('\t') for sep in f]
        fila = [x[0][0] for x in f]
        resultado =[(letra,fila.count(letra)) for letra in sorted(set(fila))]    
    return resultado


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv','r') as f:
        data = f.readlines()
        data = [fila.replace("\n", "") for fila in data]
        data = [fila.replace("\t", ",") for fila in data]
        data = [fila.split(",") for fila in data]
        data = [fila[0:2] for fila in data]
        data = [(fila[0], int(fila[1])) for fila in data] 
        respuesta =[(k, sum([y for (x,y) in data if x == k])) for k in dict(data).keys()]
        respuesta.sort(reverse = False)   
    
    return respuesta


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv','r') as f:
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]             
        fecha_mes = [t[2].split("-")[1] for t in f]
        result = [(mes, fecha_mes.count(mes)) for mes in sorted(set(fecha_mes))]
    
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv','r') as f:
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        f = [row[0:2] for row in f]
        f = [(row[0], int(row[1])) for row in f] 
        respuesta =[(k, max([y for (x,y) in f if x == k]), min([y for (x,y) in f if x == k])) for k in dict(f).keys()]
        respuesta.sort(reverse = False)    
    
    return respuesta


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open( 'data.csv' , 'r') as f:
            
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        f = [row[3:] for row in f]
        
        columna = []
        for i, element in enumerate (f):
            lista = []
            for i, fila in enumerate (element):
                if len(fila) > 1:
                    lista.append(fila)
            columna.append(lista)
        
        lista = []
        for i, element in enumerate (columna):
            lista.extend(element)
        
        lista = [(row[:3], int(row[4:])) for row in lista]
        respuesta =[(k, min([y for (x,y) in lista if x == k]), max([y for (x,y) in lista if x == k])) for k in dict(lista).keys()]
        respuesta.sort(reverse = False) 
    
    return respuesta


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open( 'data.csv' , 'r') as f:
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        f = [row[0:2] for row in f]
        f = [(int(row[1]), row[0]) for row in f] 
        
        counter = {}
        for key, value in f:
            if key in counter:       
                counter[key] += [value]
            else:
                counter[key] = [value]
        
        respuesta = [(key, counter[key]) for key in counter]
        respuesta.sort(reverse = False)
        
    return respuesta


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open( 'data.csv' , 'r') as f:
                     
        f = [fila.replace("\n", "") for fila in f ]
        f = [fila.split("\t") for fila in f ]
        
        lista = [(int(t[1]), t[0]) for t in f]
        resultado=[]
        for numero in sorted(set(t[0] for t in lista)):

            letters = sorted(set([t[1] for t in lista if t[0] == numero]))
            resultado.append((numero, letters))
            
        resultado = sorted(resultado, key=lambda x: x[0])
        
    return resultado


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open( 'data.csv' , 'r') as f:
                
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        f = [row[3:] for row in f]
        
        new_data = []
        for i, element in enumerate (f):
            lista = []
            for i, fila in enumerate (element):
                if len(fila) > 1:
                    lista.append(fila)
            new_data.append(lista)
                    
        lista = []
        for i, element in enumerate (new_data):
            lista.extend(element)
        
        lista = [row.replace(":", ",") for row in lista]    
        lista = [row.split(',') for row in lista]  
        lista = [(row[0], (int(row[1]))) for row in lista] 

        counter = {}
        for key, value in lista:
            if key in counter:       
                counter[key] += 1
            else:
                counter[key] = 1

        respuesta = list(counter.items())
        respuesta.sort(reverse = False)
        respuesta = dict (respuesta)
    
    return respuesta


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open( 'data.csv' , 'r') as f:
                
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        columna1 = [row[0] for row in f]  
        f = [row[3:] for row in f]
        
        columna4 = []
        columna5 = []
        for index, element in enumerate (f):
            lista4 = []
            lista5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    lista5.append(fila)
                if len(fila) == 1:
                    lista4.append(fila)
            columna4.append(lista4)
            columna5.append(lista5)
        
        columna4 = [len(row) for row in columna4]  
        columna5 = [len(row) for row in columna5]  
        
        respuesta =[]
        for index, element in enumerate (columna1):
            respuesta.append((str(element), columna4[index], columna5[index]))
        
    
    return respuesta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    with open( 'data.csv' , "r") as f:
           
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        columna2 = [row[1] for row in f]  
        f = [row[3:] for row in f]
        
        columna4 = []
        for index, element in enumerate (f):
            lista4 = []
            for indice, fila in enumerate (element):
                if len(fila) == 1:
                    lista4.append(fila)
            columna4.append(lista4)
        
        lista = []
        for index, element in enumerate (columna4):
            lista.extend(element)
        
        clave = set(lista)
        clave = sorted(clave)
        
        respuesta = {}
        for ind_clave, elem_clave in enumerate (clave): 
            for ind_c4, elem_c4 in enumerate(columna4):
                if elem_clave in elem_c4:
                    if elem_clave in respuesta:
                        respuesta[elem_clave] += int(columna2[ind_c4])
                    else: 
                        respuesta[elem_clave] = int(columna2[ind_c4])
    
    return respuesta

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open( 'data.csv' , "r") as f:
        
        f = [row.replace("\n", "") for row in f]
        f = [row.replace("\t", ",") for row in f]
        f = [row.split(",") for row in f]
        columna1= [row[0] for row in f]  
        f = [row[3:] for row in f]
        
        columna5 = []
        for index, element in enumerate (f):
            lista5 = []
            for indice, fila in enumerate (element):
                if len(fila) > 1:
                    lista5.append(fila)
            columna5.append(lista5)        
               
        count_column5 = [[int(e[4:]) for e in row] for row in columna5]
        count_column5 = [sum(row) for row in count_column5] 
        
        lista =[]
        for index, element in enumerate (columna1):
            lista.append((str(element), count_column5[index]))
                    
        respuesta = {}
        for key, value in lista:
            if key in respuesta:       
                respuesta[key] += value
            else:
                respuesta[key] = value        
            
        respuesta = list(respuesta.items())
        respuesta.sort(reverse = False)
        respuesta = dict (respuesta)
        
    return respuesta
