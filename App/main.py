
#llamamos archivo de mod
import utils
import read_csv
import graficas

#Ejemplo ejecucion de ejemplo con diccionario
'''
data = [
    {
        'country':'Colombia',
        'poblacion':600
    },
    {
        'country':'Chile',
        'poblacion':400
    },
    {
        'country':'Argentina',
        'poblacion':550
    },
    {
        'country':'Brasil',
        'poblacion':1200
    }
]
'''

def Run(): #modulizamos para que al ser ejecutado desde otro .py me envie solo lo solicitado
    #podemos ejecutarlo una vez llamado
    data = read_csv.read_csv('data.csv') #Llamamos el modulo con su funcion de lectura y su ubicacion para leer
    data = list(filter(lambda item:item['Continent']== 'South America',data))
    
    #RETO DE GRAFICAR UNA COLUMNA COMPLETA DE INFORMACION EN PYTHON
    countries = list(map(lambda x: x['Country/Territory'], data)) #Para obtener todos los paises usando MAP para columna
    percentages = list(map(lambda x: x['World Population Percentage'],data)) #Para obtener todos los % usando MAP para columna
    graficas.generacion_grafica_torta(countries, percentages)
    
    country = input('Type Country: ') #Vamos a solicitarlo de manera dinamica al user
    print(country)

    result =utils.poblacion_por_pais(data,country) #Generamos variable que llame la key que queremos

    if len(result) >0: #iniciamos condicion para que su tamaño sea > 0
        country = result[0]
        print(country)
        labels, values  = utils.get_poblation(country) #llamamos nuestra funcion
        graficas.generacion_grafica(country['Country/Territory'], labels, values)
    

#Permite que main.py pueda ser ejecutado desde la terminal ejecuta metodo Run pero si es desde otro archvio no lo ejecutara
#A esto le llamamos DUALIDAD
if __name__ == '__main__': 
    Run()