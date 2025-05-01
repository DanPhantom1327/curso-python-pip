#EN ESTE MODULO APRENDEREMOS A LEER ARCHIVOS CSV Y TRANSFORMAMOS LA DATA DEL ARCHIVO DADO EN UN DICCIONARIO PARA GENERAR CONSULTAS

#importamos modulo de python
import csv

def read_csv(path): #definimos funcion para lectura
    with open(path, 'r') as csvfile: #dando ubicacion y permisos de lectura
        reader = csv.reader(csvfile,delimiter=',') #diciendo que viene separado por ,
        header = next(reader) #manualmente sacamos nuestra primera fila
        data = []
        #unimeros la header con la row que se itera
        for row in reader: #generando un for para leerlo fila a fila
            iterable = zip(header, row) #los une en uno solo en un array de tuplas
            #generamos diccionario
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict) #con esto damos una lista de diccionarios con clave y valor
        return data
    
#para correrlo como un script desde la terminal
if __name__ == '__main__':
    data = read_csv('./app/data.csv') #esto nos arroja la data al terminal
    print(data)
