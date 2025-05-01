import matplotlib.pyplot as plt


#funcion para crear nuestra grafica en forma de pie
def generate_pie_chart(): 
    labels = ['A','B','C'] #cabezotes
    values = [200,34,120] #tamañ0

    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png') #guardamos en un archivo externo
    plt.close() #cerramos funcion

