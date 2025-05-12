import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #direccion(ruta) de a donde queremos hacer la solicitud
    print(r.status_code) #estado en http
    print(r.text) #retorno de informacion
    print(type(r.text)) #tipo de request
    categories = r.json() #convertir en formato JSON
    for category in categories: #Podemos hacer iteraciones
        print (category ['name'])