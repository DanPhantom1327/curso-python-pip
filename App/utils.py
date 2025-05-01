#CREAREMOS NUESTROS PROPIOS MODULOS --> son cualquier archivo que termine en .py --> podemos definir funciones,clases o variables

def poblacion_pais():
    keys = ['Col','Bol']
    values = [600,400]
    return keys, values

#Ejemplo de funcion para crear diccionario
def poblacion_por_pais(data,country):
    #creo lista con diccionario
    result = list(filter(lambda item:item['Country/Territory'] == country,data)) #filtrando que solo me de la informacion que cumpla mi condicion
    return result

#FUNCION PARA OBTENER LA POBLACION DE UN PAIS EN MI CSV
def get_poblation(country_dict):
    population_dict = { #creamos manualmente cada año
        '2022': int(country_dict['2022 Population']), #convertimos a un valor numerico ya que nos los lee como string
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
     }
    labels = population_dict.keys() #valores solicitados para graficar
    values = population_dict.values() #valores solicitados para graficar
    return labels, values