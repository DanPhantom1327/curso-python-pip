#EN ESTE MODULO APRENDEREMOS A GENERAR GRAFICAS EN PYTHON CON MOTPLOTLIB --> LIBRERIA DE PYTHON


import matplotlib.pyplot as plt#libreria que no viene incorporado en python --> debemos incorporarlo

#EJEMPLO CON DATOS FIJOS --> GRAFICA DE BARRAS

'''
def generacion_grafica(): #creamos funcion
    labels = ['a','b','c','d'] #lista de labels de la grafica
    valores = [100,200,80,130] #valores de la grafica

    fig, ax = plt.subplots() #fig = figura, ax = coordenadas graficacion
    ax.bar(labels,valores) #generaremos un grafica de barras = bar
    plt.show()

if __name__ == '__main__': #ejecutamos como un script 
    generacion_grafica()
'''

#EJEMPLO RECIBIENDO LOS DATOS --> GRAFICA DE BARRAS

#name = para darle el nombre a archivo png del pais que seleccionemos
def generacion_grafica(name, labels, valores): #creamos funcion y solicitamos los data 

    fig, ax = plt.subplots() #fig = figura, ax = coordenadas graficacion
    ax.bar(labels,valores) #generaremos un grafica de barras = bar
    plt.savefig(f'./imags/{name}.png') #damos nombre a imagen y las lanzamos a una carpeta especifica
    plt.close()
'''
if __name__ == '__main__': #ejecutamos como un script 
    labels = ['a','b','c','d'] #lista de labels de la grafica
    valores = [10,25,40,23] #valores de la grafica
    generacion_grafica(labels, valores)
'''

#EJEMPLO RECBIBIENDO DATOS -->? UNA GRAFICA DE TIPO TORTA

def generacion_grafica_torta(labels,valores):
    fig, ax = plt.subplots() #fig = figura, ax = coordenadas graficacion
    ax.pie(valores, labels=labels) #generaremos un grafica de torta = pie
    ax.axis('equal')
    plt.savefig('pie2.png')
    plt.close()



if __name__ == '__main__': #ejecutamos como un script 
    labels = ['a','b','c','d'] #lista de labels de la grafica
    valores = [10,25,40,23] #valores de la grafica
    generacion_grafica_torta(labels, valores)